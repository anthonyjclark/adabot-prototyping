
# RPi Demo
# Uses GPIO pin 32 to output voltage from HI to LOW
# Sleeps between HI and LOW to allow for human witness
# Loops an arbitrary number of times for viewing time
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT, initial=GPIO.HIGH)

for i in range(40):
	GPIO.output(32, GPIO.LOW)
	time.sleep(1.5)
	GPIO.output(32, GPIO.HIGH)
	time.sleep(1.5)
	print(i)
