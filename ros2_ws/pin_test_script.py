from gpiozero import Motor
from time import sleep


motors = [
    {"name": "Motor 1", "forward": "GPIO17", "backward": "GPIO18"},
    {"name": "Motor 2", "forward": "GPIO27", "backward": "GPIO22"},
    {"name": "Motor 3", "forward": "GPIO23", "backward": "GPIO24"},
    {"name": "Motor 4", "forward": "GPIO25", "backward": "GPIO26"},
]

# Test each motor one by one
for motor_config in motors:
    print(f"\n{'='*50}")
    print(f"Testing {motor_config['name']}")
    print(f"Forward: {motor_config['forward']}")
    print(f"Backward: {motor_config['backward']}")
    print(f"{'='*50}")
    
    input("Press ENTER to start pulsing motor...")
    
    motor = Motor(forward=motor_config["forward"], backward=motor_config["backward"])
    
    # Pulse forward until enter is pressed
    try:
        while True:
            motor.forward()
            sleep(0.5)
            motor.stop()
            sleep(0.5)
    except KeyboardInterrupt:
        pass
    
    motor.stop()
    print(f"Motor stopped.\n")

print("\nAll motor tests completed!")
