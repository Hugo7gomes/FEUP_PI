import requests
from config import *
import statistics

def getAverageWorkBlock(id):
    workBlocks = requests.get(backEndIP + '/schedules/' + str(id) + '/workBlocks')
    workBlocksHour = dict()
    if(workBlocks.status_code != 200):
        return -1
    countTime = []
    for workBlockId in workBlocks.json()["workBlockIds"]:
        workBlock = requests.get(backEndIP + '/workBlocks/' + str(workBlockId)) 
        startTime = workBlock.json()["workBlockInfo"]["start_time"]
        endTime = workBlock.json()["workBlockInfo"]["end_time"]
        countTime.append(endTime - startTime)
    
    average = statistics.mean(countTime)
    standardDeviation = statistics.stdev(countTime)
    return {'schedule': id, 'average': average, 'standardDeviation': standardDeviation}