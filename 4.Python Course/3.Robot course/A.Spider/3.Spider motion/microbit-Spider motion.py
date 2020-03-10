from microbit import *
import superbit

display.show(Image.HEART)

while True:
    superbit.motor_control_dual(superbit.M1, superbit.M3, -255, -255, 0)
    sleep(1000)

    superbit.motor_control_dual(superbit.M1, superbit.M3, 255, 255, 0)
    sleep(1000)

    superbit.motor_control_dual(superbit.M1, superbit.M3, 255, -255, 0)
    sleep(1000)

    superbit.motor_control_dual(superbit.M1, superbit.M3, -255, 255, 0)
    sleep(1000)