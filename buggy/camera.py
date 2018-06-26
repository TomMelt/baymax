from picamera import PiCamera
from time import sleep


def picture():
	
	camera = PiCamera()
	camera.start_preview()
	sleep(1)
	camera.capture('picture.jpg')
	camera.stop_preview()
	
picture()
