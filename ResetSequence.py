# -*- coding: utf-8 -*-
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
sleep(2)
Position(2)
sleep(2)
Reset()
sleep(2)
Reset()

ser.close()