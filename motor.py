__author__ = 'zackory'

import pigpio

class Motor:
    gpio = None

    def __init__(self, port1, port2):
        if Motor.gpio is None:
            Motor.gpio = pigpio.pi()
        self.port1 = port1
        self.port2 = port2
        self.isForward = True
        # Set frequency and pulse width
        Motor.gpio.set_PWM_frequency(port1, 100)
        Motor.gpio.set_PWM_frequency(port2, 100)
        Motor.gpio.set_servo_pulsewidth(port1, 0)
        Motor.gpio.set_servo_pulsewidth(port2, 0)

    # Speed between 0-255
    def setSpeed(self, speed):
        Motor.gpio.set_PWM_dutycycle(self.port2 if self.isForward else self.port1, speed)

    def setDirection(self, isForward):
        self.isForward = isForward
        self.stop()

    def stop(self):
        Motor.gpio.set_PWM_dutycycle(self.port1, 0)
        Motor.gpio.set_PWM_dutycycle(self.port2, 0)

    @staticmethod
    def stopGpio():
        Motor.gpio.stop()
