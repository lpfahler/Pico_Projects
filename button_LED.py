# Program to turn an LED on and off with a Button (momentary switch) 
# Lori Pfahler
# Feb 2023

# import modules
from machine import Pin
import utime

# setup button and LED pins
myButton = Pin(0, Pin.IN, Pin.PULL_DOWN)
myLED = Pin(1, Pin.OUT)


while True:
    # turn on/off LED when the button is pressed
    if myButton.value() == 1:
        myLED.toggle()
        # must have some sleep time to debounce the button; sleep time > 0.15
        utime.sleep(0.2)
