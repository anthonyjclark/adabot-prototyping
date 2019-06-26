New command for raspberry pi which allow to view the GPIO pin layouts:
Open a termial and type "pinout"

:This will provide a layout within the terminal of the current raspberry
pi pins.

Then head over to
<https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/> to view
documentation about how python interfaces with the raspberry pi.

You'll want to enter the python program inside the terminal and then
import **import** **RPi.GPIO** **as** **GPIO (note if you leave or exit
the python program you will need to reimport the above step)**

**\
Before beginning you must specify the pin layout you will be using this
means you will need to execute** GPIO.setmode(GPIO.BOARD)

**Next select Channel Type (note if using In you are saying you want the
pin to read whether something is high or low so Out is when you want
something to read whether a pin is high or low and this means you can
set the pin as either high or low)**

GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH) here channel is equal
to the number ie: only the whole number without any letters indicated on
the pinout layout) To check this you will you will put multimeter on the
pin with the red probe on the channel you changed and the black probe
onto ground) If the channel is set to high then red probe should read
out a value greater than 0 if the channel is set to one then the red
probe should read out 0)

Now we will work with the PWM/PCM please enter the termial and type
pinout and refer to the website pinout.xyz to see which pins are listed
as PWM.

Frequency tells us how long the square wave is

<https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/>

have

making and LED throb refer to this website for information:
<https://electronicshobbyists.com/raspberry-pi-pwm-tutorial-control-brightness-of-led-and-servo-motor/>
