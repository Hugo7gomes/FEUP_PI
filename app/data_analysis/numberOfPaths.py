import json
import requests
from config import *

def getNumberOfPaths():
    paths = requests.get(backEndIP + '/paths')
    return len(paths.json())
    