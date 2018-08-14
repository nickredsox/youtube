import serial
import numpy as np

with serial.Serial('COM4', 9600) as ser:
	x = ser.readline()
	print(x)
	
	ser.write("This is my second arduino message\n")
	
	y = ser.readline()
	print(y)
	
	ser.close()