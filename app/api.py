from flask import Flask
from flask_restful import Api
from controllers.linesController import *

app = Flask(__name__)
api = Api(app)
  

api.add_resource(Lines, '/lines')
api.add_resource(Paths, '/paths')
api.add_resource(PathLength, '/paths/<id>/length')
api.add_resource(LineLength, '/lines/<id>/length')
api.add_resource(Schedule, '/schedules/<id>/trips/hours')
api.add_resource(WorkBlock, '/schedules/<id>/workblocks/hours')
api.add_resource(AverageWorkBlock, '/schedules/<id>/workblocks/average')

if __name__ == "__main__":
    app.run(debug=True,port = 5001, host='0.0.0.0')