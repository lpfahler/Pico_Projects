# Program to check that LEDs are correctly wired for binary clock
# Lori Pfahler
# Feb 2023

from machine import Pin
import utime

myLEDs = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 19, 20, 21, 26, 27, 28)

# setup LEDs
for i in range(0, 20, 1):
    Pin(myLEDs[i], Pin.OUT)

while True:
    # turn all LEDs on
    for i in range(0, 20, 1):
        Pin(myLEDs[i]).value(1)
        
    utime.sleep(1)

    # turn all LEDs off
    for i in range(0, 20, 1):
        Pin(myLEDs[i]).value(0)

    utime.sleep(1)