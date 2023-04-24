import json
import requests
from config import *

def getNumberOfLines():
    lines = requests.get(backEndIP + '/lines')
    print(lines.json())
    return len(lines.json())
    