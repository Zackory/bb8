__author__ = 'zackory'

import pigpio

class Motor:
    gpio = None

    def __init__(self, port1, port2):
        if Motor.gpio is None:
            Motor.gpio = pigpio.pi()
        self.port1 = port1
        self.port2 = port2
        self.prevSpeed = 0
        # Set frequency and pulse width
        Motor.gpio.set_PWM_frequency(port1, 100)
        Motor.gpio.set_PWM_frequency(port2, 100)
        Motor.gpio.set_servo_pulsewidth(port1, 0)
        Motor.gpio.set_servo_pulsewidth(port2, 0)

    # Speed between -1.0 and 1.0
    def setSpeed(self, speed):
        # Actual speeds are between -255 and 255 (scale accordingly)
        if (speed < 0 < self.prevSpeed) or (self.prevSpeed < 0 < speed):
            # We have flipped directions, so set previous port to 0
            Motor.gpio.set_PWM_dutycycle(self.port2 if self.prevSpeed >= 0 else self.port1, 0)
        self.prevSpeed = speed
        Motor.gpio.set_PWM_dutycycle(self.port2 if speed >= 0 else self.port1, int(abs(speed*255)))

    def stop(self):
        Motor.gpio.set_PWM_dutycycle(self.port1, 0)
        Motor.gpio.set_PWM_dutycycle(self.port2, 0)

    @staticmethod
    def stopGpio():
        Motor.gpio.stop()
