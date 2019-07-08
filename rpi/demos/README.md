# WALKTHROUGH 

### For these exampls we will be using Python

Let us begin a walkthrough with your Pi and a brief introduction into various aspects.
First please be aware:
New command for raspberry pi which allow to view the GPIO pin layouts:  Open a terminal and type `pinout`This will provide a layout within the terminal of the current raspberry pi pins. 

Then head over to https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/ to view documentation about how python interfaces with the raspberry pi.
You’ll want to enter the python program inside the terminal and then `import RPi.GPIO as GPIO` (note if you leave or exit the python program you will need to reimport the above step)

Before beginning you must specify the pin layout you will be using this means you will need to execute 
`GPIO.setmode(GPIO.BOARD)`

Next select Channel Type (note if using IN you are saying you want the pin to read whether something is high or low.  If using OUT, you are saying you want something to read whether a pin is high or low and this means you can set the pin as either high or low) `GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)`

here channel is equal to the number i.e.: only the whole number without any letters indicated on the pinout layout) To check this you will can use the multimeter on the pin with the red probe on the channel you changed and the black probe onto ground)  If the channel is set to high then read out on multimeter should show a value greater than 0 if the channel is set to low then read out on multimeter should show 0)

Now we will work with the PWM/PCM please enter the terminal and type pinout and refer to the website pinout.xyz to see which pins are listed as PWM.

## In depth walkthrough of making a LED turn on and a LED throb

Example to make LED turn on: (Note this is not a 1-1 example you will need to alter your code as appropriate)

Make LED turn on:
https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/


Make LED throb refer to this website for information: https://electronicshobbyists.com/raspberry-pi-pwm-tutorial-control-brightness-of-led-and-servo-motor/


## Communicating With The MotorDriver DRV 8835

Go to https://www.pololu.com/product/2135 and at the bottom look at the microcontroller and motordriver layout.
-To communicate VCC must be the same voltage output as the GPIO pins (which are the pi 3 is 3.3V)
We will be using information from this github:  https://github.com/pololu/drv8835-motor-driver-rpi
Scroll down and read the documentation which will provide the command line information to import the github stuff
Then head over to:  https://github.com/pololu/drv8835-motor-driver-rpi/blob/master/pololu_drv8835_rpi.py

* This will provide the pins which are being used so you can run example.py (in this python code when you use pinout the number will correspond to the GPIO(number) side not the number only side).
* open example.py and move to delete 
