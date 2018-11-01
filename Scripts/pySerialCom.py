import serial
import time
serPort = serial.Serial('COM3',baudrate = 9600, timeout = 1)

for x in range(20):
    time.sleep(0.5)
    arduinoData = serPort.readline().decode('ascii')
    #print(type(arduinoData))
    print (arduinoData)
    if arduinoData and int(arduinoData) > 1000:
        break 
    
 