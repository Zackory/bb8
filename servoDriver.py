__author__ = 'zackory'

import time
import servo
import joystick

joy = joystick.Joystick(0)

servo1 = servo.Servo(17)
servo2 = servo.Servo(18)
servo3 = servo.Servo(22)
servo4 = servo.Servo(23)
mastServo = servo.Servo(24)

done = False
while not done:
    joy.processEvents()
    done = joy.get(joy.RBumper)

    # Update servo speed based on joystick

    LThumbY = joy.get(joy.LThumbY)
    if LThumbY <= -0.1 or LThumbY >= 0.1:
        # Update head position by moving center mast
        mastServo.setPosition(LThumbY)
    else:
        mastServo.setPosition(0)

    LThumbX = joy.get(joy.LThumbX)
    if LThumbX <= -0.1 or LThumbX >= 0.1:
        # Rotate BB-8
        servo1.setSpeed(LThumbX)
        servo2.setSpeed(LThumbX)
        servo3.setSpeed(LThumbX)
        servo4.setSpeed(LThumbX)
    else:
        # Translate BB-8
        RThumbY = joy.get(joy.RThumbY)
        if RThumbY <= -0.1 or RThumbY >= 0.1:
            servo1.setSpeed(RThumbY)
            servo3.setSpeed(-RThumbY)
        else:
            servo1.stop()
            servo3.stop()

        RThumbX = joy.get(joy.RThumbX)
        if RThumbX <= -0.1 or RThumbX >= 0.1:
            servo2.setSpeed(RThumbX)
            servo4.setSpeed(-RThumbX)
        else:
            servo2.stop()
            servo4.stop()

    time.sleep(0.05)

# for i in np.arange(-1.0, 1.0, 0.05):
#     servo1.setSpeed(i)
#     time.sleep(0.2)

try:
    joy.quitJoystick()
except:
    pass

servo1.stop()
servo2.stop()
servo3.stop()
servo4.stop()
mastServo.stop()
servo1.stopGpio()
