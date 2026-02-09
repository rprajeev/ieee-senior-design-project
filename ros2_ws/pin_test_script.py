from gpiozero import Motor
from time import sleep

motor = Motor(forward="GPIO25", backward="GPIO26")
motor.forward()
sleep(2)
motor.backward()
sleep(2)
motor.stop()
