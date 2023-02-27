# Program with a Button (momentary switch) 
# Lori Pfahler
# Feb 2023

# import modules
from machine import Pin
import utime

# setup button pin
myButton = Pin(0, Pin.IN, Pin.PULL_DOWN)
# myButton = Pin(0, Pin.IN)


while True:
    # print the button value
    print(myButton.value())
    utime.sleep(0.2)

