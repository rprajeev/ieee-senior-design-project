from gpiozero import Motor
from time import sleep


motors = [
    {"name": "Motor 1", "forward": "GPIO17", "backward": "GPIO18"},
    {"name": "Motor 2", "forward": "GPIO27", "backward": "GPIO22"},
    {"name": "Motor 3", "forward": "GPIO24", "backward": "GPIO23"},  # Inverted
    {"name": "Motor 4", "forward": "GPIO26", "backward": "GPIO25"},  # Inverted
]

# Position mapping for mecanum drive
positions = {
    "BL": motors[0],  # Motor 1 - Back Left
    "BR": motors[1],  # Motor 2 - Back Right
    "FR": motors[2],  # Motor 3 - Front Right
    "FL": motors[3],  # Motor 4 - Front Left
}

# Create motor objects
motor_objects = {pos: Motor(forward=motor["forward"], backward=motor["backward"]) 
                 for pos, motor in positions.items()}


def stop_all():
    """Stop all motors"""
    for motor in motor_objects.values():
        motor.stop()


def forward():
    """All wheels forward"""
    print("FORWARD")
    for motor in motor_objects.values():
        motor.forward()


def backward():
    """All wheels backward"""
    print("BACKWARD")
    for motor in motor_objects.values():
        motor.backward()


def turn_left():
    """Turn left - right side forward, left side backward"""
    print("TURN LEFT")
    motor_objects["FR"].forward()
    motor_objects["BR"].forward()
    motor_objects["FL"].backward()
    motor_objects["BL"].backward()


def turn_right():
    """Turn right - left side forward, right side backward"""
    print("TURN RIGHT")
    motor_objects["FL"].forward()
    motor_objects["BL"].forward()
    motor_objects["FR"].backward()
    motor_objects["BR"].backward()


def strafe_left():
    """Strafe left"""
    print("STRAFE LEFT")
    motor_objects["FR"].forward()
    motor_objects["BL"].forward()
    motor_objects["FL"].backward()
    motor_objects["BR"].backward()


def strafe_right():
    """Strafe right"""
    print("STRAFE RIGHT")
    motor_objects["FL"].forward()
    motor_objects["BR"].forward()
    motor_objects["FR"].backward()
    motor_objects["BL"].backward()


# Test sequence
movements = [
    ("Forward", forward),
    ("Turn Left", turn_left),
    ("Turn Right", turn_right),
    ("Backward", backward),
    ("Strafe Left", strafe_left),
    ("Strafe Right", strafe_right),
]

for movement_name, movement_func in movements:
    input(f"\nPress ENTER for {movement_name}...")
    movement_func()
    sleep(3)
    stop_all()

print("\nAll movement tests completed!")
