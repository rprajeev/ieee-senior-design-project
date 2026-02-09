from gpiozero import motor
from time import sleep

motor = motor(forward="GPIO17", backward="GPIO18")
motor.forward()
sleep(2)
motor.backward()
sleep(2)
motor.stop()
