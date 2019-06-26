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
