import serial
import time

time.sleep(1)

serialPort = serial.Serial("/dev/ttyACM0", 115200)

print("Sending wakeup call")
serialPort.write("\r\n\r\n")
time.sleep(2)
print("Waiting for response")
gout = serialPort.readline()
print(gout.strip())
print("Finished with initialization")


print("STARTING COMMAND 1")
serialPort.write("G0 X0 Y0 Z0\n")
gout = serialPort.readline()
print(gout.strip())
print("COMMAND 1 DONE")

print("waiting")
time.sleep(5)

print("Starting command 2")
serialPort.write("G0 X10 Y0 Z0\n")
gout = serialPort.readline()
print(gout.strip())
print("COMMAND 2 DONE\n")

print("Starting command 3")
serialPort.write("G0 X10 Y10 Z0\n")
gout = serialPort.readline()
print(gout.strip())
print("COMMAND 3 DONE")

print("Starting command 4")
serialPort.write("G0 X10 Y10 Z10\n")
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
