from picamera import PiCamera
import pygame
import pygame.camera
from time import sleep


class Image:
    # path = path to where the image will be saved i.e. /home/pi/Desktop/Image.jpg
    # camera = picamera object
    def getImage(self, path, camera):
        camera.start_preview()
        camera.capture(path)
	#raw_input()
        camera.stop_preview()
        return

    # camera = pygame.camera.Camera object
    # path = path to where the image will be saved i.e. /home/pi/Desktop/Image.jpg
    def getPyGameImage(self, camera, path):
        camera.get_controls()
        camera.start()
        image = camera.get_image()
        camera.stop()
        pygame.image.save(image, path)
        return

