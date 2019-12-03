import random
import math

class detectLugNuts:
    def getPoints(self, numPoints, scale):
        MAX_HEIGHT = 300
        MAX_WIDTH = 400
        MAX_RADIUS = 150
        radius = random.randrange(25, MAX_RADIUS, 1)
        center_y = random.randrange(-MAX_HEIGHT + radius, MAX_HEIGHT - radius, 1)
        center_x = random.randrange(-MAX_WIDTH + radius, MAX_WIDTH - radius, 1)

        scale_y = 1
        scale_x = 1
        if scale:
            scale_y = random.randrange(20, 100, 1)/100
            scale_x = random.randrange(20, 100, 1)/100


        angle = 360/numPoints

        currentAngle = angle*random.random()

        pointList = []

        for i in range(numPoints):
            x = radius*math.cos(math.radians(currentAngle))
            x = (x*scale_x) + center_x

            y = radius*math.sin(math.radians(currentAngle))
            y = (y*scale_y) + center_y

            point = (x,y)
#             print(point)
            pointList.append(point)
            currentAngle += angle

        return pointList
