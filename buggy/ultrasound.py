from gpiozero import DistanceSensor
from time import sleep


def Distance(sleeptime=0.1):
    sensor = DistanceSensor(echo=18, trigger=17)
    distance = sensor.distance * 100
    sleep(sleeptime)
    return distance
