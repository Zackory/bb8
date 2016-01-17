__author__ = 'zackory'

import pigpio

class Servo:
    gpio = None

    def __init__(self, port):
        if Servo.gpio is None:
            print 'Creating Servo GPIO'
            Servo.gpio = pigpio.pi()
        self.port = port
        # Set frequency and pulse width
        Servo.gpio.set_PWM_frequency(port, 100)
        Servo.gpio.set_servo_pulsewidth(port, 0)

    # Speed between -1.0 and 1.0
    def setSpeed(self, speed):
        # Set servo pulse width to adjust speed of continuous servo
        # Safe range (1000-2000), <1500 backwards, >1500 forwards, 1500 stopped (max range of 500-2500)
        Servo.gpio.set_servo_pulsewidth(self.port, 0 if speed == 0 else 1500 + speed*500)

    # Position between -1.0 and 1.0
    def setPosition(self, position):
        # Set servo pulse width to adjust position of fixed rotation servo
        # 1500 center point (max range 500-2500, safe range 1000-2000)
        Servo.gpio.set_servo_pulsewidth(self.port, 1500 + position*500)

    def stop(self):
        Servo.gpio.set_servo_pulsewidth(self.port, 0)

    @staticmethod
    def stopGpio():
        Servo.gpio.stop()
