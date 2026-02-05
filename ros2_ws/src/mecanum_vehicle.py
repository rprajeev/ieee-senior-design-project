# ================================
# TOGGLE THIS LINE
# ================================
# front left wheel pin 5 - forward, 6 - backward
# front right wheel pin 13 - forward, 19 - backward
# rear left wheel pin 12 - forward, 16 - backward
# rear right wheel pin 20 - forward, 21 - backward
# front pwm pin 18, rear pwm pin 23
USE_MOCK = True   # <-- set to False when motors are wired
# ================================

if USE_MOCK:
    # ---------------- MOCK HARDWARE ----------------
    class Motor:
        def __init__(self, forward=None, backward=None):
            self.forward_pin = forward
            self.backward_pin = backward

        def forward(self):
            print(f"[MOCK] Motor({self.forward_pin},{self.backward_pin}) -> FORWARD")

        def backward(self):
            print(f"[MOCK] Motor({self.forward_pin},{self.backward_pin}) -> BACKWARD")

        def stop(self):
            print(f"[MOCK] Motor({self.forward_pin},{self.backward_pin}) -> STOP")


    class PWMOutputDevice:
        def __init__(self, pin):
            self.pin = pin
            self._value = 0.0

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, v):
            self._value = v
            print(f"[MOCK] PWM(pin={self.pin}) = {v}")

else:
    # ---------------- REAL HARDWARE ----------------
    from gpiozero import Motor, PWMOutputDevice


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

    def _set_motor(self, motor, direction):
        if direction > 0:
            motor.forward()
        elif direction < 0:
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

    def forward(self, speed=0.4):
        self.drive(1, 1, 1, 1, speed)

    def rotate_cw(self, speed=0.4):
        self.drive(1, -1, 1, -1, speed)
