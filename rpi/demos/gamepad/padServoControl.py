from select import select
import wiringpi
import evdev
from evdev import InputDevice, categorize, ecodes

servo_pulse = 150
should_extend = False
should_retract = False
pulse_increment = 5
MAX_SERVO_PULSE = 200
MIN_SERVO_PULSE = 100

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds type
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)




#create object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event2')

count = 150
a_string = "*"

while True:
    r, _, _ = select([gamepad], [], [], 0.1)

    if r:
        for event in gamepad.read():
            if event.code == ecodes.BTN_TR2:
                if event.value == 1:
                    print("down")
                    should_retract = True
                elif event.value == 0:
                    print("up")
                    should_retract = False
            if event.code == ecodes.BTN_TR:
                if event.value == 1:
                    print("down")
                    should_extend = True
                elif event.value == 0:
                    print("up")
                    should_extend = False

    if should_extend:
       # if len(a_string) < 10:
        if count < 200:
            a_string = " " + a_string
            count += 5
        servo_pulse += pulse_increment
        servo_pulse = min(servo_pulse, MAX_SERVO_PULSE)
    elif should_retract:
       # if len(a_string) > 1:
        if count > 100:
            a_string = a_string[1:]
            count -= 5
        servo_pulse -= pulse_increment
        servo_pulse = max(servo_pulse, MIN_SERVO_PULSE)
    #print(servo_pulse)
    print((servo_pulse - 100)//5 * "*")
    wiringpi.pwmWrite(18, servo_pulse)


"""
for event in gamepad.read_loop():
    if event.code == 312:
        print("TriggerLeft2 ")
    if event.code == ecodes.BTN_TL:
        print("TriggerLeft1 ",event.value)


async def helper(dev):
    async for ev in dev.async_read_loop():
        print(repr(ev))

loop = asyncio.get_event_loop()
loop.run_until_complete(helper(gamepad))


while True:
    if should_extend:
        servo_pulse += pulse_increment
        servo_pulse = max(servo_pulse, MAX_SERVO_PULSE)
    print(servo_pulse)
"""
