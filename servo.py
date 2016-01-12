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
        # Determine direction of motion
        if speed < 0: # backwards
            Servo.gpio.set_servo_pulsewidth(self.port, 1000)
        elif speed > 0: # forwards
            Servo.gpio.set_servo_pulsewidth(self.port, 2000)
        else: # stopped
            Servo.gpio.set_servo_pulsewidth(self.port, 0)

        # Actual speeds are between -255 and 255 (scale accordingly)
        Servo.gpio.set_PWM_dutycycle(self.port, int(abs(speed*255)))

    def stop(self):
        Servo.gpio.set_PWM_dutycycle(self.port, 0)

    @staticmethod
    def stopGpio():
        Servo.gpio.stop()
