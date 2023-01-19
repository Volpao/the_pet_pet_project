from flask import jsonify, request
from flask_restful import Resource
import tensorflow as tf
import numpy as np 
from PIL import Image
from keras.applications.xception import preprocess_input
from keras.models import load_model
import io
import base64


supported_extensions = ["jpg", "jpeg", "png"]
model = load_model('final_model.h5')



class Predict(Resource):
    def post(self):
        # image_from_request = request.files['image']
        message = request.get_json(force=True)
        try:
            image = self.load_image(message)
        except:
            return jsonify({"error": "Your file extension is not supported or too small. Please load a jpeg, jpg or png file."})

        result = self.predict(model, image)
        return jsonify({"result": result})

    def load_image(self, message):
        
        encoded = message['image']
        decoded = base64.b64decode(encoded)
        img = Image.open(io.BytesIO(decoded))
        print(img)
        if img.format.lower() not in supported_extensions:
            raise Exception()
        img = img.convert('RGB')
        img = img.resize((299,299), Image.NEAREST)
        tensor = tf.convert_to_tensor(img, dtype=tf.float32)
        batch = np.expand_dims(tensor, axis = 0)
        batch = batch.copy()
        batch = preprocess_input(batch)
        return batch

    def predict(self, clf, image):
        probs = clf.predict(image)
        cls = np.argmax(probs, axis = 1)
        if cls[0]==0:
            return 'AKITA INU'
        elif cls[0]==1:
            return 'SIBERIAN HUSKY'
        elif cls[0]==2:
            return 'OTHER BREED'
        else:
            return 'SHIBA INU'