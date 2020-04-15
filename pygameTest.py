import time
import pygame
import pygame.camera


pygame.init()
pygame.camera.init()

cam1 = pygame.camera.Camera("/dev/video0", (1280, 720))
#cam2 = pygame.camera.Camera("/dev/video2", (1280, 720))

window = pygame.display.set_mode((1280, 720),pygame.RESIZABLE)

num = 101


while True:
	# Take picture with camera 1
	cam1.get_controls()
	cam1.start()
	image = cam1.get_image()
	cam1.stop()

	window.blit(image, (0,0))
	pygame.display.update()

	pygame.image.save(image, "/home/pi/Desktop/BoltImages/" + str(num) + ".jpg")
	num += 1
	print(num)
	time.sleep(0.3)

#	# Take picture with camera 2
#	cam2.get_controls()
#	cam2.start()
#	image = cam2.get_image()
#	cam2.stop()

#	window.blit(image, (0,0))
#	pygame.display.update()

#	pygame.image.save(image, "/home/pi/Desktop/BoltImages/" + str(num) + ".jpg")
#	num += 1
#	print(num)
#	time.sleep(0.3)
