try:
    from gpiozero import Motor, PWMOutputDevice
except Exception:
    # gpiozero not available (e.g. not running on Raspberry Pi); provide lightweight stubs for testing
    class Motor:
        def __init__(self, forward=None, backward=None):
            self._state = 0
        def forward(self):
            self._state = 1
        def backward(self):
            self._state = -1
        def stop(self):
            self._state = 0

    class PWMOutputDevice:
        def __init__(self, pin, active_high=True, initial_value=0.0):
            self._value = float(initial_value)
        @property
        def value(self):
            return self._value
        @value.setter
        def value(self, v):
            self._value = float(v)
        def close(self):
            pass


class MecanumVehicle:
    def __init__(self):
        # Front motors (L298 #1)
        self.fl = Motor(forward=5, backward=6)
        self.fr = Motor(forward=13, backward=19)
        self.front_pwm = PWMOutputDevice(18)

        # Rear motors (L298 #2)
        self.rl = Motor(forward=12, backward=16)
        self.rr = Motor(forward=20, backward=21)
        self.rear_pwm = PWMOutputDevice(23)

    def _set_motor(self, motor, value):
        if value > 0:
            motor.forward()
        elif value < 0:
            motor.backward()
        else:
            motor.stop()

    def drive(self, fl, fr, rl, rr, speed):
        self._set_motor(self.fl, fl)
        self._set_motor(self.fr, fr)
        self._set_motor(self.rl, rl)
        self._set_motor(self.rr, rr)

        self.front_pwm.value = speed
        self.rear_pwm.value = speed

    def stop(self):
        self.drive(0, 0, 0, 0, 0)

    # High-level movements
    def forward(self, speed=0.4):
        self.drive(1, 1, 1, 1, speed)

    def backward(self, speed=0.4):
        self.drive(-1, -1, -1, -1, speed)

    def strafe_right(self, speed=0.4):
        self.drive(1, -1, -1, 1, speed)

    def strafe_left(self, speed=0.4):
        self.drive(-1, 1, 1, -1, speed)

    def rotate_cw(self, speed=0.4):
        self.drive(1, -1, 1, -1, speed)

    def rotate_ccw(self, speed=0.4):
        self.drive(-1, 1, -1, 1, speed)
