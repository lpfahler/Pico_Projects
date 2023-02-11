# Program for a Binary Counter 0-15 Version 2
# Lori Pfahler
# Feb 2023

from machine import Pin
from utime import sleep
# variable for setting the speed of counting
delayTime = 2
# setup the four LEDs
onePlaceLED = Pin(12, Pin.OUT)
twoPlaceLED = Pin(13, Pin.OUT)
fourPlaceLED = Pin(14, Pin.OUT)
eightPlaceLED = Pin(15, Pin.OUT)

# use try and except to turn LEDs off when exiting the program
try:
    while True:
        for myNum in range(0, 16, 1):
            # turn myNum into binary string with four digits
            myBin = '{0:04b}'.format(myNum)
            print(myBin, '=', myNum)
            # light up the LEDS according to the binary representation
            # separate out digits of the binary string and make these integers
            eightPlaceLED.value(int(myBin[0]))
            fourPlaceLED.value(int(myBin[1]))
            twoPlaceLED.value(int(myBin[2]))
            onePlaceLED.value(int(myBin[3]))
            # a sleep to see the counting
            sleep(delayTime)
            
except KeyboardInterrupt:
    # turn off LEDs
    eightPlaceLED.off()
    fourPlaceLED.off()
    twoPlaceLED.off()
    onePlaceLED.off()
