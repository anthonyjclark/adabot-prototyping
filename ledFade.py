from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
p = GPIO.PWM(32, 100) #frequency
p.start(30) #duty cycle
p.ChangeDutyCycle(80)
p.ChangeFrequency(1000)
duty_cycle = 0
for count in range(40):
	if count % 2 == 0:
		duty_cycle_inc = 5
	else:
		duty_cycle_inc = -5
	for i in range(20):
		p.ChangeDutyCycle(duty_cycle)
		sleep(.05) #4 sec
		duty_cycle += duty_cycle_inc
input("Press return to stop: ")
p.stop()
GPIO.cleanup()


