from gpiozero import Motor
from time import sleep

# Motor pin mappings (BOARD to GPIO conversion)
# Motor 1: BOARD 11 (GPIO17), BOARD 12 (GPIO27)
# Motor 2: BOARD 13 (GPIO22), BOARD 15 (GPIO23)
# Motor 3: BOARD 16 (GPIO24), BOARD 18 (GPIO25)
# Motor 4: BOARD 22 (GPIO26), BOARD 37 (GPIO26)

motors = [
    {"name": "Motor 1", "forward": "GPIO17", "backward": "GPIO27"},
    {"name": "Motor 2", "forward": "GPIO22", "backward": "GPIO23"},
    {"name": "Motor 3", "forward": "GPIO24", "backward": "GPIO25"},
    {"name": "Motor 4", "forward": "GPIO26", "backward": "GPIO12"},
]

# Test each motor
for motor_config in motors:
    print(f"\nTesting {motor_config['name']}...")
    motor = Motor(forward=motor_config["forward"], backward=motor_config["backward"])
    
    print(f"  Forward...")
    motor.forward()
    sleep(2)
    
    print(f"  Backward...")
    motor.backward()
    sleep(2)
    
    print(f"  Stopped.")
    motor.stop()
    sleep(1)

print("\nAll motor tests completed!")
