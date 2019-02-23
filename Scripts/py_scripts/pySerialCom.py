import serial
import time
serPort = serial.Serial('COM5',baudrate = 9600, timeout = 1)

for x in range(1000):
    time.sleep(0.2)
    arduinoData = serPort.readline()#.decode('ascii')
    #print(type(arduinoData))
    print (arduinoData)
    #print (arduinoData.rstrip("\n"))

    #if arduinoData and int(arduinoData) > 1000:
    #    break 
    
 