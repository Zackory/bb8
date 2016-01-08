__author__ = 'zackory'

import time
import motor
import joystick

joy = joystick.Joystick(0)

motor1 = motor.Motor(25, 18)
# motor2 = motor.Motor(23, 24)

motor1.setDirection(True)
for i in xrange(0, 260, 5):
    motor1.setSpeed(i)
    time.sleep(0.2)

motor1.setDirection(False)
for i in xrange(0, 260, 5):
    motor1.setSpeed(i)
    time.sleep(0.2)

joy.quitJoystick()

motor1.stop()
# motor2.stop()
motor1.stopGpio()
