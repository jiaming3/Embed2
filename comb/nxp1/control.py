import time
from bmp280 import bmp280_readdata,bmp280_convert,bmp280_checktemp
from si import hum,temp
from motor import init,forward,reverse,stop
import RPi.GPIO as gpio


def right(tf):
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(tf)
    gpio.cleanup()

def funcclk(times,time):

        for x in range(1,times):#how many times rotate per day
            right(time)#here, set time to control the rotation time(angle)
            time.sleep(86400/times)#time interval between each rotation

def funcsensor():
    data = bmp280_readdata(0x77)
    p = bmp280_convert(data)
    t = bmp280_checktemp(data)
    te = temp()
    hu = hum()
    booldone=False
    counter=0
    while booldone=False:
        if te > 35 and couter <2:
            reverse(x)  # set x manually here to control the time of operation
            counter=counter+1
        elif hu > 80 and couter <2:
            reverse(x)
            counter = counter + 1
        elif p > 1005.7 and couter <2:
            reverse(x)
            counter = counter + 1
        else:
            pass
    time.sleep(1800)
    counter=0;















