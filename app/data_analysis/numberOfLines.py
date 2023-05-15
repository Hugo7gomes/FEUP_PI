import requests
from config import *

def getNumberOfLines():
    lines = requests.get(backEndIP + '/lines')
    print(len(lines.json()))
    return len(lines.json())
    