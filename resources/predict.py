import os
from flask import jsonify, request
from flask_restful import Resource
import tensorflow as tf
import numpy as np 
from PIL import Image
from keras.applications.xception import preprocess_input
from keras.models import load_model



supported_extensions = ["jpg", "jpeg", "png"]
model = load_model('final_model.h5')



class Predict(Resource):
    def post(self):
        image_from_request = request.files['image']
        try:
            image = load_image(image_from_request.stream)
        except:
            return jsonify({"error": "Your file extension is not supported or too small. Please load a jpeg, jpg or png file."})
        result = predict(model, image)
        
        return jsonify({"result": result})

def load_image(image_bytes):
    img = Image.open(image_bytes)
    if img.format.lower() not in supported_extensions:
        raise Exception()
    img = img.convert('RGB')
    img = img.resize((299,299), Image.NEAREST)
    img = tf.convert_to_tensor(img, dtype=tf.float32)
    img = np.expand_dims(img, axis = 0)
    img = img.copy()
    img = preprocess_input(img)
    return img

def predict(clf, image):
    probs = clf.predict(image)
    cls = np.argmax(probs, axis = 1)
    if cls[0]==0:
        return 'Akita inu'
    elif cls[0]==1:
        return 'Siberian husky'
    elif cls[0]==2:
        return 'Other breed'
    else:
        return 'Shiba inu'