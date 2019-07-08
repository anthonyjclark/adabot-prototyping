from __future__ import print_function
import time
from pololu_drv8835_rpi import motors, MAX_SPEED

# using setmode(GPIO.BCM) instead of GPIO.BOARD
# GPIO12 = Board 32 PWM pin


# GPIO pin sets direction (forward, reverse)
# PWM pin sets the speed (handled by library)

try:

    for i in range(10):
        motors.setSpeeds(0, 0) # calling class Motors (motor1 speed, motor2 speed)
        print("sleeping for 2 seconds")
        time.sleep(4)          # sleep for 2 seconds
        motors.setSpeeds(MAX_SPEED, MAX_SPEED) 
        print(MAX_SPEED, " (max speed) for 2 seconds")
        time.sleep(4)
        motors.setSpeeds(-MAX_SPEED, -MAX_SPEED)
        print(-MAX_SPEED, " reversing!!!")
        time.sleep(4)

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
  motors.setSpeeds(0, 0)
