from picamera import PiCamera
from time import sleep

class Image:
    def getImage(self, path):
        camera = PiCamera()
        camera.start_preview()
        camera.capture(path)
        camera.stop_preview()
        return
