import time
import pygame
import pygame.camera


pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0", (1000, 1000))

window = pygame.display.set_mode((1000, 1000),pygame.RESIZABLE)

num = 1

while True:
	cam.get_controls()
	cam.start()
	image = cam.get_image()
	cam.stop()

	window.blit(image, (0,0))
	pygame.display.update()

	pygame.image.save(image, "/home/pi/Desktop/BoltImages/" + str(num) + ".jpg")
	num += 1
	print(num)
	time.sleep(1)
