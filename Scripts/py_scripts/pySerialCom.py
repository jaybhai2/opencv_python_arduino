import serial
import time
# import matplotlib.pyplot as pyplot
# import matplotlib.animation as animation
# from matplotlib import style
import numpy as np

mywindow = 10
thres=80
def sma(data,window):
    weights = np.repeat(1.0,window)/window
    smas = np.convolve(data,weights,'valid')
    # if len(sma) < mywindow:
    #     return 0
    # else: 
    return smas
serPort = serial.Serial('COM5',baudrate = 9600, timeout = 1)
freq = 0

# fig = pyplot.figure()
# ax1 = fig.add_subplot(1,1,1)
# fig.show()

x, y = [], []
# time.sleep(5)

for x1 in range(1,1000,1):
    time.sleep(0.01)
    period = serPort.readline().decode('ascii')
    period = period.strip()

    if len(period) > 1:
        time0 = int(period)
        #if(tim > 0):
        #freq = int(tim)
        # freq = int(5000/tim*1000000-10000)
        

        x.append(time0)
        #print(sma(x,mywindow))
        if len(x) > mywindow+1:
            movingave = int(sma(x,mywindow)[len(x)-mywindow-1])
            
            diffT =abs(time0 - movingave)
            if diffT > thres:
                diffT = str(diffT) + "!!!!!!!!!!!!"
            
            print(str(time0) + ' ' + str(movingave) + ' ' + str(diffT))

        else:
            print(time0)
        # y.append(time0)
        # ax1.plot(x,y,color='b')
        # fig.canvas.draw()
        # ax1.set_xlim(left=max(0, time1-10),right = time1+10)

    # time.sleep(0.2)
