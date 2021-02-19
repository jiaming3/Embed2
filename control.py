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
    if te>35:
        reverse(x)#set x manually here to control the time of operation
    elif hu>80:
        reverse(x)
    elif p>1005.7:
        reverse(x)
    else:
        pass














