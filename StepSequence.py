# -*- coding: utf-8 -*-
import numpy as np
import serial
from time import sleep

#Define commands
def Position(pos):
    string = "POS "+ str(pos)+ " 1\n"
    ser.write(bytes(string, 'UTF-8'))

def Reset():
    ser.write(bytes("RESET 1\n", 'UTF-8'))
    

#setup the serial port
usbport = 'COM4'
ser = serial.Serial(usbport, 9600, timeout=1) 

#Sequence
Reset()
sleep(3.5)
for i in np.arange(0, 10):
    Position(2)
    sleep(0.5)
    Position(1)
    sleep(0.5)    
    Position(3)
    sleep(0.5)
    Position(1)
    sleep(0.5)

ser.close()