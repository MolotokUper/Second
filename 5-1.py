import RPi.GPIO as gpi
import time


def f(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def Voltage(num):
    global dac
    for i, val in enumerate(f(num)):
        gpi.output(dac[i], val)

def adc():
    global dac, comp
    first, last = 0, 255
    for i in range(8):
        voltage = first +(last - first)//2
        Voltage(voltage)
        time.sleep(0.07)
        if not gpi.input(comp):
            last = voltage
        else:
            first = voltage
    return 3.3*(first +(last - first)//2)/255            

gpi.setmode(gpi.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gpi.setup(comp, gpi.IN)
gpi.setup(dac, gpi.OUT)
gpi.setup(troyka, gpi.OUT, initial = 1)


try:
    while True:
        print(adc())
finally:
    gpi.output(dac, 0)
    gpi.cleanup()
