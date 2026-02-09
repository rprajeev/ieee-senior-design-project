from gpiozero import Motor
from time import sleep

motor = Motor(forward="GPIO23", backward="GPIO24")
motor.forward()
sleep(2)
motor.backward()
sleep(2)
motor.stop()
