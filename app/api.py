from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort
from controllers.linesController import *

app = Flask(__name__)
api = Api(app)
  

api.add_resource(Lines, '/lines')
api.add_resource(Paths, '/paths')
api.add_resource(PathLength, '/paths/<id>/length')
api.add_resource(LineLength, '/lines/<id>/length')
  
if __name__ == "__main__":
    app.run(debug=True)