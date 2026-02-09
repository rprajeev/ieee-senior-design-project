# ================================
# Motor pin assignments
# ================================
# front left wheel pin 11 - forward, 12 - backward
# front right wheel pin 13 - forward, 15 - backward
# rear left wheel pin 16 - forward, 18 - backward
# rear right wheel pin 22 - forward, 37 - backward
# H-bridge connections shorted: PWM pins bypassed
# ================================

from gpiozero import Motor


class MecanumVehicle:
    def __init__(self):
        # Front motors (L298 #1)
        self.fl = Motor(forward=11, backward=12)
        self.fr = Motor(forward=13, backward=15)

        # Rear motors (L298 #2)
        self.rl = Motor(forward=16, backward=18)
        self.rr = Motor(forward=22, backward=37)

    def _set_motor(self, motor, direction):
        if direction > 0:
            motor.forward()
        elif direction < 0:
            motor.backward()
        else:
            motor.stop()

    def drive(self, fl, fr, rl, rr, speed=1.0):
        self._set_motor(self.fl, fl)
        self._set_motor(self.fr, fr)
        self._set_motor(self.rl, rl)
        self._set_motor(self.rr, rr)

    def stop(self):
        self.drive(0, 0, 0, 0, 0)

    def forward(self, speed=0.4):
        self.drive(1, 1, 1, 1, speed)

    def rotate_cw(self, speed=0.4):
        self.drive(1, -1, 1, -1, speed)
