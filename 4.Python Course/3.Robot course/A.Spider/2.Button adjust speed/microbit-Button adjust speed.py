from microbit import *

import microbit
import superbit

display.show(Image.HAPPY)
a = 0

def limit_change():
    global a
    if microbit.button_a.is_pressed():
        a = a + 50
        if a > 255:
            a = 255
    if microbit.button_b.is_pressed():
        a = a - 50
        if a < 0:
            a = 0
    return

while True:
    limit_change()
    superbit.motor_control(superbit.M1, -a, 0)
    sleep(500)