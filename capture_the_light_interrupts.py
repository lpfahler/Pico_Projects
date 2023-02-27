# Program to play Capture the Light Game with interrupts and debouncing
# Lori Pfahler
# Feb 2023

from machine import Pin
import utime
import random

# setup the button pin
button = Pin(0, Pin.IN, Pin.PULL_DOWN)

# how fast the lights are moving initially
delayTime = 0.07
# range for how fast the light will move from LED to LED
# Using random function to make it harder for the user
# to time the button press
delayTimeMin = 0.03
delayTimeMax = 0.12

# create an empty list to hold the LED Pin info
LEDlist = []
# setup LEDs - 13 LEDs in my circuit
for i in range(1, 14, 1):
    # i is the GPIO pin number: 1-13
    LEDname = 'LED'+str(i)
    LEDname = Pin(i, Pin.OUT)
    LEDlist.append(LEDname)

# turn off the LEDs from a previous "bad" run   
for i in LEDlist:
    i.value(0)

# define interrupt handler fuction that does button debouncing
def button_handler(button):
    global interrupt_flag, debounce_time
    if (utime.ticks_ms()-debounce_time) > 300:
        interrupt_flag= 1
        debounce_time=utime.ticks_ms()
    
interrupt_flag=0
debounce_time=0

button.irq(trigger = Pin.IRQ_RISING, handler = button_handler)

# variables needed to cycle through the LEDs
index = 0
step = 1

try:
    while True:
        # 13 LEDS in circuit - they are contained in 0-12 positions in LEDlist
        if index == 12:  
            step = -1
        elif index == 0:
            step = 1
        LEDlist[index].value(1)
        utime.sleep(delayTime)
        LEDlist[index].value(0)
        if interrupt_flag == 1:
            interrupt_flag=0
            # light the LED that was lit when the button was pushed
            LEDlist[index].value(1)
            # give feedback on game results
            if index ==5 or index == 7:
                print('Good!')
            elif index == 6:
                print('Excellent!')
            else:
                print('Try Again!')
            print('Restarting in 5 seconds')
            print('Press <crtl><c> to end the game\n')
            utime.sleep(5)
            # turn off led
            LEDlist[index].value(0)
            # reset index and step
            index = -1
            step = 1
        index += step
        # add in some differing speeds
        delayTime = random.uniform(delayTimeMin, delayTimeMax)    


except KeyboardInterrupt:
    print('Thanks for playing!')
    for i in LEDlist:
        i.value(0)  