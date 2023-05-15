import requests
from config import *

def getPathLength(id):  
    paths_segs = requests.get(backEndIP + '/paths/segs')
    paths = requests.get(backEndIP + '/paths/' + str(id))
    emptyLength = 0 
    length = 0
    for segments in paths_segs.json()['pathsSegs']:
        if segments['path_version_id'] == int(id) and (paths.json()['pathInfo']['empty'] == True):
            emptyLength += segments['length']
        if segments['path_version_id'] == int(id) and (paths.json()['pathInfo']['empty'] == False):
            length += segments['length']
    return {'pathId': id, 'emptyLength': emptyLength, 'length': length}
    



        
    

    