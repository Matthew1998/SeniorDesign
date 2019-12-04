from interpretImage import interpretImage
from ObjectDetector import ObjectDetector
#from getImage import Image
import turtle
from PIL import Image

#create objects
objectDetector = ObjectDetector('models/lugnut/')
interpret = interpretImage()
#pic = Image()

imagePath = "IMG_1414.jpg"
imageGIF = imagePath.replace('.jpg', '.gif')

#set up turtle perameters
wn = turtle.Screen()
wn.setup(600, 450)
bg = Image.open(imagePath).convert('RGB').rotate(180).save(imageGIF)
wn.bgpic(imageGIF)
wn.update()
wn.title("Polygon")

turt = turtle.Turtle()
turt.penup()
turt.shape("turtle")
turt.pencolor("yellow")

#pic.getImage('/home/seniordesign/Desktop/picture.jpg')

objectDetector.detectObject('lugnutDetection/images/IMG_1414.jpg')
objectDetector.filterDetections(0.5)


#get the bolt loacations and plot them
small_l = objectDetector.getBoxCenters()
l  = []
for point in small_l:
	newp = ((point[0]-0.5)*600, (0.5-point[1])*450)
	l.append(newp)

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

turt.goto(-300, -225)

#output information
print("Position is: ")
print(avg)
print("Angle is: ")
print(angle)

turtle.done()

exit()