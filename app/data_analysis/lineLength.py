import json
from .pathLength import getPathLength, getEmptyPath
import requests
from config import *

def getLineLength(line_number):
    lines = requests.get(backEndIP + '/lines/' + line_number)
    if(lines.status_code != 200):
        return -1
    id_line = lines.json()['lineInfo']['id']
    lines_paths = requests.get(backEndIP + '/lines/' + str(id_line) + '/paths')
    length = 0 
    for id_path in lines_paths.json()['pathIds']:
        length += getEmptyPath(id_path)
    return length