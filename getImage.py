from picamera import PiCamera
from time import sleep

class Image:
    def getImage(self):
        camera = PiCamera()
        camera.start_preview()
        camera.capture('/home/pi/Desktop/picture.jpg')
        camera.stop_preview()
        return
