import RPi.GPIO as gpi

dac = [21, 20, 16, 12, 7, 8, 25, 24]
gpi.setmode(gpi.BCM)
gpi.setup(22, gpi.OUT)


def f(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]


try:
    while True:
        print("Input a number from 0 to 255")
        res = input()
        if res == "q":
            print("Have a nice day!")
            exit()
        try:
            n = int(res)
        except ValueError:
            print("Isn't digit number")
        else:
            gpi.output(dac, f(n))
            print("Power in Volt is", n / 255 * 3.3)
finally:
    gpi.output(dac, 0)
    gpi.cleanup()
