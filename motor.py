__author__ = 'zackory'

import pigpio

class Motor:
    gpio = None

    def __init__(self, port1, port2):
        if Motor.gpio is None:
            Motor.gpio = pigpio.pi()
        self.port1 = port1
        self.port2 = port2
        # Set frequency and pulse width
        Motor.gpio.set_PWM_frequency(port2, 100)
        Motor.gpio.set_servo_pulsewidth(port1, 0)

    # Speed between 0-255
    def setSpeed(self, speed):
        Motor.gpio.set_PWM_dutycycle(self.port2, speed)

    def stop(self):
        Motor.gpio.set_PWM_dutycycle(self.port2, 0)

    def stopGpio(self):
        Motor.gpio.stop()
