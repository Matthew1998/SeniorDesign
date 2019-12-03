from interpretImage import interpretImage
from detectLugNuts import detectLugNuts
from getImage import Image
import turtle

#create objects
pattern = detectLugNuts()
interpret = interpretImage()
pic = Image()

#set up turtle perameters
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Polygon")
turt = turtle.Turtle()
turtle.screensize(800,600)
turt.penup()
turt.shape("turtle")

pic.getImage()

#get the bolt loacations and plot them
l = pattern.getPoints(5, True)
for point in l:
    turt.goto(point[0], point[1])
    turt.dot()

#fond and plot the center point
avg = interpret.findAverage(l)
turt.goto(avg[0], avg[1])
turt.dot()

#find the normalized points and plot them
normalizedPoints = interpret.normalizePoints(l)
turt.pencolor("red")
for point in normalizedPoints:
    turt.goto(point[0], point[1])
    turt.dot()

#plot the center of the normal polygon
newAvg = interpret.findAverage(normalizedPoints)
turt.goto(newAvg[0], newAvg[1])
turt.dot()

#find the offset angle of the wheel
angle = interpret.getAngleOffset(normalizedPoints)

turt.goto(-100, -100)

#output information
print("Position is: ")
print(avg)
print("Angle is: ")
print(angle)

turtle.done()

exit()