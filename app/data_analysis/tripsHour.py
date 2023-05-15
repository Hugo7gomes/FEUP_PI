import json
import requests
from config import *


def getTripsHour(id):
    trips = requests.get(backEndIP + '/schedules/' + str(id) + '/trips')
    tripsHour = dict()
    if(trips.status_code != 200):
        return -1
        
    for tripId in trips.json()["tripIds"]:
        trip = requests.get(backEndIP + '/trips/' + str(tripId)) 
        hour = trip.json()["tripInfo"]["start_time"] // 3600
        if(hour in tripsHour):
            tripsHour[hour] += 1
        else:
            tripsHour[hour] = 1
    result = []
    for i in range(24):
        trip = dict()
        trip['ti'] = i * 3600
        trip['tf'] = (i + 1) * 3600
        if(i not in tripsHour):
            trip['value'] = 0
        else:
            trip['value'] = tripsHour[i]

        result.append(trip)

    return {'schedule': id, 'data': result}
            

        

    