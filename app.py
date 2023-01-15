from flask import Flask
from flask_restful import Api

from env import SECRET_KEY
from resources.predict import Predict

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = SECRET_KEY
api = Api(app)

api.add_resource(Predict, '/predict')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)
