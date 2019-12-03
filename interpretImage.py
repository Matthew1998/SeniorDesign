import math

class interpretImage:
    def findAverage(self, l):
        length = len(l)
        sumx = 0
        sumy = 0
        for i in range(length):
            sumx += l[i][0]
            sumy += l[i][1]
        avgx = sumx/length
        avgy = sumy/length
        return (avgx,avgy)

    def findRMS(self, l):
        length = len(l)
        sumx = 0
        sumy = 0
        avg = self.findAverage(l)
        for point in l:
            sumx += abs(point[0]-avg[0])
            sumy += abs(point[1]-avg[1])
        avgx = sumx/length
        avgy = sumy/length
        return (avgx+avg[0], avgy+avg[1])

    def normalizePoints(self, l):
        avg = self.findAverage(l)
        RMS = self.findRMS(l)
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

    def getAngleOffset(self, l):
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
