# This file will simulate the image detection results until the image detection is ready to go.

from shapely.geometry import LineString
import random
import math
import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Polygon")
turt = turtle.Turtle()
turtle.screensize(800,600)
turt.penup()
turt.shape("turtle")


def getPoints(numPoints, scale):
    MAX_HEIGHT = 300
    MAX_WIDTH = 400
    MAX_RADIUS = 150
    center_y = MAX_HEIGHT*random.random()
    center_x = MAX_WIDTH*random.random()
    radius = MAX_RADIUS*random.random()

    scale_y = 1
    scale_x = 1
    if scale:
        scale_y = random.random()
        scale_x = random.random()


    angle = 360/numPoints

    currentAngle = angle*random.random()

    pointList = []

    for i in range(numPoints):
        x = radius*math.cos(math.radians(currentAngle))
        x = (x*scale_x) + center_x

        y = radius*math.sin(math.radians(currentAngle))
        y = (y*scale_y) + center_y

        point = (x,y)
        print(point)
        turt.goto(x,y)
        turt.dot()
        pointList.append(point)
        currentAngle += angle

    return pointList

# def findCentroid (l):
#     length = len(l)
#     if (length == 5):
#         shape = LineString([(l[0][0],l[0][1]),(l[1][0],l[1][1]),(l[2][0],l[2][1]),(l[3][0],l[3][1]),(l[4][0],l[4][1])])
#         c = shape.centroid
#         print(c)
#     elif (length == 4):
#         shape = LineString([(l[0][0],l[0][1]),(l[1][0],l[1][1]),(l[2][0],l[2][1]),(l[3][0],l[3][1])])
#         c = shape.centroid
#         print(c)
#     else:
#    #centerList = center.split()
# #centerX = float(centerList[1][1:])
# #centerY = float(centerList[2][:-1])
# #turt.goto(center.x,center.y)
#      print("not 5")
#     return c;

def findAverage(l):
    length = len(l)
    sumx = 0
    sumy = 0
    for i in range(length):
        sumx += l[i][0]
        sumy += l[i][1]
    avgx = sumx/length
    avgy = sumy/length
    return (avgx,avgy)

def findRMS(l):
    length = len(l)
    sumx = 0
    sumy = 0
    avg = findAverage(l)
    for point in l:
        sumx += abs(point[0]-avg[0])
        sumy += abs(point[1]-avg[1])
    avgx = sumx/length
    avgy = sumy/length
    return (avgx+avg[0], avgy+avg[1])

def normalizePoints(l):
    avg = findAverage(l)
    RMS = findRMS(l)
    slope = (RMS[1]-avg[1])/(RMS[0]-avg[0])
    
    transformedPoints = []
    for point in l:
        x = point[0] - avg[0]
        y = point[1] - avg[1]
        newP = (x,y)
        transformedPoints.append(newP)
     
    expandedPoints = []

    if slope < 1:
        for point in transformedPoints:
            x = point[0]
            y = point[1]/slope
            newP = (x, y)
            expandedPoints.append(newP)
            
    else:
        for point in transformedPoints:
            x = point[0]*slope
            y = point[1]
            newP = (x, y)
            expandedPoints.append(newP)
            
    return expandedPoints

def getAngleOffset(l):
    highestPoint = [0,0]
    for point in l:
        if point[1] > highestPoint[1]:
            highestPoint = point
    angle = math.degrees(math.atan(highestPoint[1]/highestPoint[0])) - 90
    if highestPoint[0] < 0:
        angle += 180;
    elif highestPoint[1] < 0:
        angle += 360
    return angle



l = getPoints(5, True)

avg = findAverage(l)
turt.goto(avg[0], avg[1])
turt.dot()

normalizedPoints = normalizePoints(l)

for point in normalizedPoints:
    turt.goto(point[0], point[1])
    turt.dot()
    
newAvg = findAverage(normalizedPoints)
turt.goto(newAvg[0], newAvg[1])
turt.dot()

angle = getAngleOffset(normalizedPoints)

turt.goto(-100, -100)

print("Position is: ")
print(avg)

print("Angle is: ")
print(angle)

turtle.done()

