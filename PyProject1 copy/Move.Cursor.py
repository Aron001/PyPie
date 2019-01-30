from pynput.mouse import Controller
from time import sleep

mouse = Controller()

for minutes in range(120):
    sleep(10)
    mouse.move = (100, -100)
    print("Movement")
    if minutes % 5 == 0:
        mouse.position = (500,500)
        print("Initialization")




