import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinTrigger = 17
pinEcho = 27

print("ultrasonic measurement")
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)


def measure():
    while True:
        GPIO.output(pinTrigger, True)
        print(GPIO.input(pinEcho))
#    flag = 0
#    receive = 0
#    timestart = time.time()
#
#    while flag == 0:
#        GPIO.output(pinTrigger, True)
#
#        if GPIO.input(pinEcho) == 1:
#            flag = 1
#            receive = 1
#            GPIO.output(pinTrigger, False)
#        elif (time.time()-timestart) > 2:
#            flag = 1
#            GPIO.output(pinTrigger, False)
#        else:
#            continue
#    return flag, receive


GPIO.cleanup()
