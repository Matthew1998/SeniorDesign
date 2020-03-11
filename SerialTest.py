import serial
import time

feedrate = 300
time.sleep(1)

serialPort = serial.Serial("/dev/ttyACM0", 115200)

print("Sending wakeup call")
serialPort.write("\r\n\r\n")
time.sleep(2)
print("Waiting for response")
gout = serialPort.readline()
print(gout.strip())
print("Finished with initialization")

print("Reseting Zero Position")
serialPort.write("G92 X0 Y0 Z0\n")
gout = serialPort.readline()
print(gout.strip())
print("Reset DONE")

print("Setting up for circle")
serialPort.write("G0 X3 Y0 Z0\n")
gout = serialPort.readline()
print(gout.strip())
print("Circle setup done")

while True:
    print("CIRCLE TIME!")
    serialPort.write("G2 X-3 Y0 R3 F" + str(feedrate) + "\n")
    gout = serialPort.readline()
    print(gout.strip())
    serialPort.write("G2 X3 Y0 R3 F" + str(feedrate) + "\n")
    gout = serialPort.readline()
    print(gout.strip())
    print("Circle Sent")
    time.sleep(8)

print("STARTING COMMAND 1")
serialPort.write("G0 X0 Y0 Z0\n")
gout = serialPort.readline()
print(gout.strip())
print("COMMAND 1 DONE")

print("waiting")
time.sleep(5)

print("Starting command 2")
serialPort.write("G0 X1 Y0 Z0\n")
gout = serialPort.readline()
print(gout.strip())
print("COMMAND 2 DONE\n")

print("Starting command 3")
serialPort.write("G0 X1 Y1 Z0\n")
gout = serialPort.readline()
print(gout.strip())
print("COMMAND 3 DONE")

print("Starting command 4")
serialPort.write("G0 X1 Y1 Z1\n")
gout = serialPort.readline()
print(gout.strip())
print("COMMAND 4 DONE")

print("Starting command 5")
serialPort.write("G0 X0 Y0 Z0\n")
gout = serialPort.readline()
print(gout.strip())
print("COMMAND 5 DONE")

serialPort.close()
print("\n\nDONE!!")
