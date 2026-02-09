from gpiozero import Motor
from time import sleep

motor = Motor(forward="BOARD11", backward="BOARD12")
motor.forward()
sleep(2)
motor.backward()
sleep(2)
motor.stop()
