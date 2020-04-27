import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution=(1024,786)
    camera.start_preview()
    time.sleep(2)
    camera.capture('image.jpg')
    camera.stop_preview()