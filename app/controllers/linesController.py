from flask import Flask, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from data_analysis.numberOfLines import getNumberOfLines
from data_analysis.numberOfPaths import getNumberOfPaths
from data_analysis.pathLength import getPathLength
from data_analysis.lineLength import getLineLength
from data_analysis.tripsHour import getTripsHour


class PathLength(Resource):
    def get(self, id):
        return getPathLength(id)

class Lines(Resource):
    def get(self):
        return getNumberOfLines()
    

class Paths(Resource):
    def get(self):
        return getNumberOfPaths()
    
class LineLength(Resource):
    def get(self, id):
        response = getLineLength(id)
        if(response == -1):
            return make_response(jsonify({'error': 'Line does not exist'}), 404)
        
        return response, 200
    
class Schedule(Resource):
    def get(self, id):
        response = getTripsHour(id)
        if(response == -1):
            return make_response(jsonify({'error': 'Line does not exist'}), 404)
        
        return response, 200
       
    


