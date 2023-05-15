from flask import Flask, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from data_analysis.numberOfLines import getNumberOfLines
from data_analysis.numberOfPaths import getNumberOfPaths
from data_analysis.pathLength import getPathLength
from data_analysis.lineLength import getLineLength
from data_analysis.tripsHour import getTripsHour
from data_analysis.workBlockHours import getWorkBlockHour
from data_analysis.averageWorkBlock import getAverageWorkBlock


class PathLength(Resource):
    def get(self, id):
        response = getPathLength(id)
        if(response == -1):
            return make_response(jsonify({'error': 'Path does not exist'}), 404)
        return make_response(response, 200)

class Lines(Resource):
    def get(self):
        response = getNumberOfLines()
        if(response == -1):
            return make_response(jsonify({'error': 'Line does not exist'}), 404)
        return make_response(response, 200)
    

class Paths(Resource):
    def get(self):
        response = getNumberOfPaths()
        if(response == -1):
            return make_response(jsonify({'error': 'Path does not exist'}), 404)
        return make_response(response, 200)
    
class LineLength(Resource):
    def get(self, id):
        response = getLineLength(id)
        if(response == -1):
            return make_response(jsonify({'error': 'Line does not exist'}), 404) 
        return make_response(response, 200)
    
class Schedule(Resource):
    def get(self, id):
        response = getTripsHour(id)
        if(response == -1):
            return make_response(jsonify({'error': 'Line does not exist'}), 404)
        return make_response(response, 200)
       
    

class WorkBlock(Resource):
    def get(self, id):
        response = getWorkBlockHour(id)
        if(response == -1):
            return make_response(jsonify({'error': 'Line does not exist'}), 404)
        return make_response(response, 200)

class AverageWorkBlock(Resource):
    def get(self, id):
        response = getAverageWorkBlock(id)
        if(response == -1):
            return make_response(jsonify({'error': 'Line does not exist'}), 404)
        return make_response(response, 200)

