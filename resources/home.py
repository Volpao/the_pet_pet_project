from flask import Response
from flask_restful import Resource
from flask import  render_template


class Home(Resource):
    def get(self):
        return Response(render_template("predict.html"),  mimetype='text/html')