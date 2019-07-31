# RPi Demo using PWM
# Fades an LED in and out
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 100)   # starting frequency
p.start(30)         # starting duty cycle
p.ChangeDutyCycle(80)
p.ChangeFrequency(1000)
duty_cycle = 0
for count in range(40):     # loop for how many times you want program to run
    if count % 2 == 0:      # every other time...
        duty_cycle_inc = 5  # fade in LED
    else:
        duty_cycle_inc = -5 # fade out LED
    for i in range(20):     # loop to change duty cycle and pause for viewing
        p.ChangeDutyCycle(duty_cycle)
        sleep(.05)          # 15 ms
        duty_cycle += duty_cycle_inc
input("Press return to stop: ")
p.stop()
GPIO.cleanup()


