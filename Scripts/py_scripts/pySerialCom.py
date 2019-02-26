import serial
import time



serPort = serial.Serial('COM5',baudrate = 9600, timeout = 1)
freq = 0

for x1 in range(1000):

    time.sleep(0.2)
    arduinoData = serPort.readline().decode('ascii')
    arduinoData = arduinoData.strip()
    
    if len(arduinoData) > 1:
        tim = int(arduinoData)
       
    
        if(tim > 0):
            freq = int(tim)
            # freq = int(5000/tim*1000000-10000)
            print(freq-69500)

  


    

 