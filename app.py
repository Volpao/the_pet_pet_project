from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from env import SECRET_KEY
from resources.predict import Predict
from resources.home import Home

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = SECRET_KEY
CORS(app)
api = Api(app)

api.add_resource(Predict, '/predict')
api.add_resource(Home, '/')



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port='5001', debug=True)
