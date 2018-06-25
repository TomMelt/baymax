import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinMotorAForwards=10
pinMotorABackwards=9
pinMotorBForwards=7
pinMotorBBackwards=8

#define three speeds
normal=50
fast=100
slow=20
Stop=0

Frequency=50

scale=1#calibration of the two motors



GPIO.setup(pinMotorAForwards,GPIO.OUT)
GPIO.setup(pinMotorABackwards,GPIO.OUT)
GPIO.setup(pinMotorBForwards,GPIO.OUT)
GPIO.setup(pinMotorBBackwards,GPIO.OUT)

#define cycles
pwmMotorAForwards=GPIO.PWM(pinMotorAForwards,Frequency)
pwmMotorABackwards=GPIO.PWM(pinMotorABackwards,Frequency)
pwmMotorBForwards=GPIO.PWM(pinMotorBForwards,Frequency)
pwmMotorBBackwards=GPIO.PWM(pinMotorBBackwards,Frequency)

#turn off all motors
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

#def turn off



def stopmotors():
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	
	
def forwards(DutyCycle=normal):
	pwmMotorAForwards.ChangeDutyCycle(DutyCycle)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycle*scale)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)

def backwards(DutyCycle=normal):
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycle)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycle*scale)
	
def left(DutyCycle=normal):
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycle)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycle*scale)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	
def right(DutyCycle=normal):
	pwmMotorAForwards.ChangeDutyCycle(DutyCycle)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycle*scale)
#backwards(slow)
#time.sleep(2)

right(slow)
time.sleep(1)

#forwards()
#time.sleep(1)

#right()
#time.sleep(0.5)

#backwards()
#time.sleep(0.5)

stopmotors()	

	

GPIO.cleanup()
