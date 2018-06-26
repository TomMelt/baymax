from picamera import PiCamera
from time import sleep


def picture():
    name = 'picture.jpg'
    camera = PiCamera()
    camera.start_preview()
    sleep(1)
    camera.capture(name)
    camera.stop_preview()
    return name
