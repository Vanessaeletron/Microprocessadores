#!/usr/bin/env python2

import serial, time

ser = serial.Serial("COM3", timeout=.1, baudrate = 9600)
#ser.port = "/dev/ttyACM0" # may be called something different
#ser.baudrate = 9600
time.sleep(1) #give the connection a second to settle
ser.open
time.sleep(1) #give the connection a second to settle
print('A:')
print(ser.isOpen())
if ser.isOpen():
	while True:
		ser.write("0")
		time.sleep(0.5)
		ser.write("1")
		time.sleep(0.1)
		ser.write("0")
		time.sleep(0.1)
		ser.write("1")
		time.sleep(0.1)
		ser.write("0")
		time.sleep(0.1)
		ser.write("1")
		time.sleep(0.1)

# import serial, time
# ser = serial.Serial()
# ser.port = "/dev/ttyUSB0" # may be called something different
# ser.baudrate = 115200 # may be different
# ser.open()
# if ser.isOpen():
#     ser.write("hello")
#     response = ser.read(ser.inWaiting())
