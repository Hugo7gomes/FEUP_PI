import json
import requests
#import sys
#sys.path.insert(1, '../')
from config import *

def getPathLength(id):  
    paths_segs = requests.get(backEndIP + '/paths/segs')
    paths = requests.get(backEndIP + '/paths/' + str(id))
    length = 0 
    for segments in paths_segs.json()['pathsSegs']:
        if segments['path_version_id'] == int(id) and (paths.json()['pathInfo']['empty'] == False):
            length += segments['length']
    return length
    

def getEmptyPath(id):
    paths_segs = requests.get(backEndIP + '/paths/segs')
    paths = requests.get(backEndIP + '/paths/' + str(id))
    length = 0 
    for segments in paths_segs.json()['pathsSegs']:
        if segments['path_version_id'] == int(id) and (paths.json()['pathInfo']['empty'] == True):
            length += segments['length']
    return length
        
    

    