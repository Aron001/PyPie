from pynput.mouse import Controller
from time import sleep
from random import randint

mouse = Controller()

for minutes in range(120):
    sleep(60)
    x, y = randint(0, 1000), randint(0, 1000)
    mouse.position = (x, y)
    print("Movement")





