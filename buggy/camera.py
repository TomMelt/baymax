from picamera import PiCamera
from time import sleep


def picture():
    name = 'picture.jpg'
    outfile = open(name, 'w')
    camera = PiCamera()
    camera.start_preview()
    sleep(1)
    camera.capture(outfile)
    camera.stop_preview()
    outfile.close()
    camera.close()
    return name
