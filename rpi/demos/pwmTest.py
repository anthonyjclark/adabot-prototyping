# RPi Demo
# Using PWM, pin 32 as output
# Demonstrates a constant flow of ~1.65 volts (~half of ~3 volts)
# line 9, "50" is 50% of the voltage it can give (~3 volts)
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
p = GPIO.PWM(32, 10000) # 10000 is frequency in Hz (makes the wave go faster; its period)
p.start(50) # 50 is the duty cycle Range[1,100] (how much time inside period you are high)
input("Press return to stop: ")
p.stop()
GPIO.cleanup()

