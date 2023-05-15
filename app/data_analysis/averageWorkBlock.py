import requests
from config import *

def getAverageWorkBlock(id):
    workBlocks = requests.get(backEndIP + '/schedules/' + str(id) + '/workBlocks')
    workBlocksHour = dict()
    if(workBlocks.status_code != 200):
        return -1
    
    for workBlockId in workBlocks.json()["workBlockIds"]:
        workBlock = requests.get(backEndIP + '/workBlocks/' + str(workBlockId)) 
        hour = workBlock.json()["workBlockInfo"]["start_time"] // 3600
        if(hour in workBlocksHour):
            workBlocksHour[hour] += 1
        else:
            workBlocksHour[hour] = 1
    result = []
    for i in range(24):
        workBlock = dict()
        workBlock['ti'] = i * 3600
        workBlock['tf'] = (i + 1) * 3600
        if(i not in workBlocksHour):
            workBlock['value'] = 0
        else:
            workBlock['value'] = workBlocksHour[i]

        result.append(workBlock)

    return {'schedule': id, 'data': result}