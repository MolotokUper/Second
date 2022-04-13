import RPi.GPIO as gpi

dac = [21, 20, 16, 12, 7, 8, 25, 24]
gpi.setmode(gpi.BCM)
gpi.setup(22, gpi.OUT)
gpi.setup(dac, gpi.OUT, initial = 1)



try:
    while True:
        gpi.setup(dac, gpi.OUT, initial = 1)
        print("Input chastota")
        n = int(input())
        p = gpi.PWM(22, n)
        print("Input duty cycle:")
        d = int(input())
        p.start(d)
        print(d * 3.3 / 100)
        input("Press")
        p.stop()
        gpi.cleanup()
finally:
    gpi.output(dac, 0)
    gpi.cleanup()
