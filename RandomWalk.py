# -*- coding: utf-8 -*-
import numpy as np
import serial
from time import sleep

#Define commands
def Position(pos):
    string = "POS "+ str(pos)+ " 1\n"
    ser.write(bytes(string, 'UTF-8'))
    

#setup the serial port
usbport = 'COM4'
ser = serial.Serial(usbport, 9600, timeout=1) 

RandomPositions=np.random.random_integers(1, 5, 30)

ser.write(bytes("RESET 1\n", 'UTF-8'))
for Filter in RandomPositions:
    Position(Filter)
    sleep(0.5)

ser.write(bytes("RESET 1\n", 'UTF-8'))
ser.close()