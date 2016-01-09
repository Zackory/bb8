__author__ = 'zackory'

import time
import motor
import joystick
import numpy as np

joy = joystick.Joystick(0)

motor1 = motor.Motor(25, 18)
# motor2 = motor.Motor(23, 24)

done = False
while not done:
    joy.processEvents()
    done = joy.get(joy.RBumper)

    # Update motor speed based on joystick
    RThumbY = joy.get(joy.RThumbY)
    if RThumbY <= -0.1 or RThumbY >= 0.1:
        motor1.setSpeed(RThumbY)
    else:
        motor1.stop()

    time.sleep(0.05)

# for i in np.arange(-1.0, 1.0, 0.05):
#     motor1.setSpeed(i)
#     time.sleep(0.2)

joy.quitJoystick()

motor1.stop()
# motor2.stop()
motor1.stopGpio()
