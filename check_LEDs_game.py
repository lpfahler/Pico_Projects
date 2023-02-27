# Program to check that LEDs are correctly wired for capture the light game
# Lori Pfahler
# Feb 2023

from machine import Pin 
import utime

delayTime = 1

# create an empty list to hold the LED Pin info
LEDlist = []
# setup LEDs - 13 LEDs in my circuit
for i in range(1, 14, 1):
    # i is the GPIO pin number: 1-13
    LEDname = 'LED'+str(i)
    LEDname = Pin(i, Pin.OUT)
    LEDlist.append(LEDname)

while True:
    for i in LEDlist:
        i.toggle()
    utime.sleep(delayTime)       
        
    
    
