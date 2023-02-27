# Program to make the LEDs cycle back and forth
# Lori Pfahler
# Feb 2023

from machine import Pin 
import utime
import random

# setup button
myButton = Pin(0, Pin.IN, Pin.PULL_DOWN)

# how fast the lights are moving
delayTime = 0.2

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
        print('index =', index, 'step =', step, 'LED =', LEDlist[index])
        LEDlist[index].value(1)
        utime.sleep(delayTime)
        LEDlist[index].value(0)
        index += step
        # add in some differing speeds
        delayTime = random.uniform(0.1, 0.2)

except KeyboardInterrupt:
    for i in LEDlist:
        i.value(0)
        

        