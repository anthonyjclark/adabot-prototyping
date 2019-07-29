# adabot-prototyping

**PIN LAYOUT**

* **New Command For Raspberry Pi Which Allows Viewing Of The GPIO Pin Layout**
    * 1) Open a terminal and type `pinout`
            * This will provide a layout within the terminal of the raspberry pi pins

    * 2) To view documentation about how python interfaces with rasberry pi follow the link <https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/ >

    * 3) In the python IDE we need to import **GPIO**
            * In python type `import RPi.GPIO as GPIO` 
                * Note if we leave or exit the python program without saving we will need to reimport the above step

**GPIO PIN LAYOUT**

* **Before Beginning We Will Specify The Pin Layout** 
    * 1) In python type `GPIO.setmode(GPIO.BOARD)`

    * 2) Next we will select Channel Type
            *  Note if using **Channel IN** found in step 3 as `GPIO.IN` we are saying we want the pin to read whether something is high or low.  
            *  Note if using **Channel OUT** found in step 3 as `GPIO.OUT` we are saying we want something to read whether a pin is high or low which means we can set the pin as either high or low 
        
    * 3) To set channel type `GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)`
        
    * 4) When viewing this website: <https://pinout.xyz/> the pins we'll be using are the  number(s) found closet to the rectangle which have the Yellow Circles above and below it.
            * To check this we will use the multimeter on the pin with the red probe on the pin number and the black probe onto ground  
            * If the channel is set to high then read out on multimeter should show a value greater than 0 
            * If the channel is set to low then read out on multimeter should show 0

**PWM/PCM PINS**

* **Now We Will Work With The PWM/PCM** 

    * 1) Enter the terminal and type `pinout` and refer to  <https://pinout.xyz/> to see which pins are listed as PWM.

* **Making A LED Turn On And A LED Throb**

    * This is an example showing how to operate a LED.  This example is not 1-1 as some of the code will likely need to be modified 
       
        **Make LED Turn On**
            
        1) Follow the link to see instructions for making a LED turn on <https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/>
        
        **Make LED Throb**
            
        1) Follow the link to see instructions for making a LED throb <https://electronicshobbyists.com/raspberry-pi-pwm-tutorial-control-brightness-of-led-and-servo-motor/>

**COMMUNICATING WITH THE MOTORDRIVER DRV 8835**

* 1) Go to <https://www.pololu.com/product/2135> and scroll down the page until ***"Using the motor driver"*** and examine how microcontroller and motordriver connect.
        *   To communicate VCC must be the same voltage output as the GPIO pins which on the rasberry pi 3B+ is 3.3V
        * Information from this github:  <https://github.com/pololu/drv8835-motor-driver-rpi> will provide the command line information to import the github stuff
        * Then head over to:  <https://github.com/pololu/drv8835-motor-driver-rpi/blob/master/pololu_drv8835_rpi.py>
            * This will provide the pins which are being used to run [&lt;example.py&gt;](https://github.com/pololu/drv8835-motor-driver-rpi/blob/master/example.py)
            * In this python code when using `pinout` the number will correspond to the **wiringpi** layout as found here: <https://pinout.xyz/pinout/wiringpi> 
* 2) Open [&lt;example.py&gt;](https://github.com/pololu/drv8835-motor-driver-rpi/blob/master/example.py) and move to delete 
