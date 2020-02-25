from picamera import PiCamera
from time import sleep

class Image:
    def getImage(self, path, number=0):
        camera = PiCamera(camera_num=number)
        camera.start_preview()
        camera.capture(path)
	raw_input()
        camera.stop_preview()
        return
