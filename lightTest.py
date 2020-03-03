import time
from neopixel import *
import argparse


matrixList = [[  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15]
             ,[ 31,  30,  29,  28,  27,  26,  25,  24,  23,  22,  21,  20,  19,  18,  17,  16]
             ,[ 32,  33,  34,  35,  36,  37,  38,  39,  40,  41,  42,  43,  44,  45,  46,  47]
             ,[ 63,  62,  61,  60,  59,  58,  57,  56,  55,  54,  53,  52,  51,  50,  49,  48]
             ,[ 64,  65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,  78,  79]
             ,[ 95,  94,  93,  92,  91,  90,  89,  88,  87,  86,  85,  84,  83,  82,  81,  80]
             ,[ 96,  97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]
             ,[127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112]
             ,[128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]
             ,[159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144]
             ,[160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175]
             ,[191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176]
             ,[192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207]
             ,[223, 222, 221, 220, 219, 218, 217, 216, 215, 214, 213, 212, 211, 210, 209, 208]
             ,[224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239]
             ,[255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, 244, 243, 242, 241, 240]]



# LED strip configuration:
LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 40     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def crosshairLocation(x,y):
	"""Display Crosshair"""
	if 0 > x > 14:
		return
	elif 0 > y > 14:
		return
	else:
		strip.setPixelColor(matrixList[y][x], Color(20, 190, 60))
	        strip.setPixelColor(matrixList[y+1][x], Color(20, 190, 60))
	        strip.setPixelColor(matrixList[y][x+1], Color(20, 190, 60))
	        strip.setPixelColor(matrixList[y+1][x+1], Color(20, 190, 60))
		strip.show()

def targetBox(color='red'):
	"""Display Box"""
	if color == 'red':
		C = Color(0, 150, 0)
	elif color == 'yellow':
		C = Color(100, 100, 0)
	elif color == 'green':
		C = Color(150, 0, 0)
	elif color == 'drag':
		C = Color(20, 190, 60)
	else:
		C = Color(0, 0, 255)

	for i in range(6, 10):
		strip.setPixelColor(matrixList[i][6], C)
		strip.setPixelColor(matrixList[6][i], C)
		strip.setPixelColor(matrixList[9][i], C)
		strip.setPixelColor(matrixList[i][9], C)

	strip.show()

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print 'Press Ctrl-C to quit.'

	"""
	while True:
		# Color wipe animations.
		colorWipe(strip, Color(255, 0, 0))  # Red wipe
		colorWipe(strip, Color(0, 255, 0))  # Blue wipe
		colorWipe(strip, Color(0, 0, 255))  # Green wipe
		# Theater chase animations.
		theaterChase(strip, Color(127, 127, 127))  # White theater chase
		theaterChase(strip, Color(127,   0,   0))  # Red theater chase
		theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
		# Rainbow animations.
		rainbow(strip)
		rainbowCycle(strip)
		theaterChaseRainbow(strip)"""

	"""
        for i in range(16):
	#	strip.setPixelColor(matrixList[i][i], Color(0, 200, 0))
	#	strip.show()
	#	time.sleep(0.05)
		crosshairLocation(i, i)

	for i in range(16):
	#	strip.setPixelColor(matrixList[15-i][i], Color(0, 200, 0))
	#	strip.show()
	#	time.sleep(0.05)
		crosshairLocation(15-i, i)
	"""

	targetBox(color='drag')


