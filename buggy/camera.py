from picamera import PiCamera
from time import sleep


def picture():
    name = 'picture.jpg'
    with open(name, 'w') as outfile:
        camera = PiCamera()
        camera.start_preview()
        sleep(1)
        camera.capture(outfile)
        camera.stop_preview()
        camera.close()
    return name
