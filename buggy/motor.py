import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 7
pinMotorBBackwards = 8

# define three speeds
_normal = 50
_fast = 100
_slow = 20
_Stop = 0

_dist_unit = 1
_turn_unit = 1./270.

Frequency = 50

# calibration of the two motors
scale = 1

GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# define cycles
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# turn off all motors
pwmMotorAForwards.start(_Stop)
pwmMotorABackwards.start(_Stop)
pwmMotorBForwards.start(_Stop)
pwmMotorBBackwards.start(_Stop)


def stopmotors():
    pwmMotorAForwards.ChangeDutyCycle(_Stop)
    pwmMotorABackwards.ChangeDutyCycle(_Stop)
    pwmMotorBForwards.ChangeDutyCycle(_Stop)
    pwmMotorBBackwards.ChangeDutyCycle(_Stop)


def goForward(DutyCycle=_normal):
    pwmMotorAForwards.ChangeDutyCycle(DutyCycle)
    pwmMotorABackwards.ChangeDutyCycle(_Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycle*scale)
    pwmMotorBBackwards.ChangeDutyCycle(_Stop)


def goBack(DutyCycle=_normal):
    pwmMotorAForwards.ChangeDutyCycle(_Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycle)
    pwmMotorBForwards.ChangeDutyCycle(_Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycle*scale)


def turnLeft(DutyCycle=_normal):
    pwmMotorAForwards.ChangeDutyCycle(_Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycle)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycle*scale)
    pwmMotorBBackwards.ChangeDutyCycle(_Stop)


def turnRight(DutyCycle=_normal):
    pwmMotorAForwards.ChangeDutyCycle(DutyCycle)
    pwmMotorABackwards.ChangeDutyCycle(_Stop)
    pwmMotorBForwards.ChangeDutyCycle(_Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycle*scale)


def moveB(distance=1, speed=_normal):
    goBack(DutyCycle=speed)
    time.sleep(distance*_dist_unit)
    stopmotors()


def moveF(distance=1, speed=_normal):
    goForward(DutyCycle=speed)
    time.sleep(distance*_dist_unit)
    stopmotors()


def moveR(angle=90, speed=_normal):
    turnRight(DutyCycle=speed)
    time.sleep(angle*_turn_unit)
    stopmotors()


def moveL(angle=90, speed=_normal):
    turnLeft(DutyCycle=speed)
    time.sleep(angle*_turn_unit)
    stopmotors()


#if __name__ == "__main__":

#    moveF(distance=1, speed=_normal)

#    GPIO.cleanup()
