import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
p = GPIO.PWM(32, 10000) #10000 is frequency Hz (makes the wave go faster) period
p.start(50) #50 is the duty cycle Range(1,100) (how much time inside period you are high)
input("Press return to stop: ")
p.stop()
GPIO.cleanup()

