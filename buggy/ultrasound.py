from gpiozero import DistanceSensor
from time import sleep
import numpy as np


def Distance(sleeptime=0.1):
    sensor = DistanceSensor(echo=18, trigger=17)
    distance = sensor.distance * 100
    sleep(sleeptime)
    return distance


def AverageDistance(sleeptime=0.1):
    events = []
    for i in range(10):
        d = Distance(sleeptime=sleeptime)
        events.append(d)
    events = np.array(events)
    return np.average(events)
