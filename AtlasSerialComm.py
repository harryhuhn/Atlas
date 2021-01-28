from datetime import time

import serial
arduinoData = serial.Serial('com3', 9600)

#def ledOn():
    #arduinoData.write(b'1') #may need to put write(b'1') since this is python3
def watch():
    arduinoData.write(b'2')
def commConfirm():
    arduinoData.write(b'0')
def liftOff():
    arduinoData.write(b'1')



