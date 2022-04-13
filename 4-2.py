import RPi.GPIO as gpi
import time


dac = [21, 20, 16, 12, 7, 8, 25, 24]
gpi.setmode(gpi.BCM)
gpi.setup(22, gpi.OUT)


def f(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]



try:
    for k in range(3):
        print('time period?:')
        period = int(input())
        for i in range(255):
            gpi.output(dac, f(i))
            time.sleep(period / 510)
            print("Power in Volts is:", i / 255 * 3.3)
        for i in range(255, 0, -1):
            gpi.output(dac, f(i))
            time.sleep(period / 510)
            print("Power in Volt is", i / 255 * 3.3)
except ValueError:
    print("GoodBye")
finally:
    gpi.output(dac, 0)
    gpi.cleanup()