from gpiozero import Motor
from time import sleep

# -------------------------
# MOTOR SETUP
# -------------------------

motor1 = Motor(17, 18)
motor2 = Motor(27, 22)
motor3 = Motor(23, 24)
motor4 = Motor(25, 26)

# Adjust this for your slower motor
SLOW_MOTOR_SCALE = 1.10

BASE_SPEED = 0.8

# -------------------------
# MOVEMENT FUNCTIONS
# -------------------------

def move_forward(speed):
    motor1.forward(speed)
    motor2.forward(speed)
    motor3.forward(speed)
    motor4.forward(speed * SLOW_MOTOR_SCALE)

def turn_right(speed):
    motor1.forward(speed)
    motor2.backward(speed)
    motor3.forward(speed)
    motor4.backward(speed * SLOW_MOTOR_SCALE)

def stop_all():
    motor1.stop()
    motor2.stop()
    motor3.stop()
    motor4.stop()

# -------------------------
# MAIN SEQUENCE
# -------------------------

FORWARD_TIME = 2.5   # replace with your calibrated value
TURN_TIME = 1.0      # calibrate for 90° turn

# Move 20 inches
move_forward(BASE_SPEED)
sleep(FORWARD_TIME)
stop_all()

sleep(5)

# Turn
turn_right(0.7)
sleep(TURN_TIME)
stop_all()

sleep(1)

# Continue forward
move_forward(BASE_SPEED)
sleep(FORWARD_TIME)
stop_all()

print("Path complete.")
