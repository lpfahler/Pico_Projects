# Program for a Binary Counter 0-15 Version 1
# Lori Pfahler
# Feb 2023

from machine import Pin
from utime import sleep
# variable for setting the speed of counting
delayTime = 2
# setup the four LEDs
eightPlaceLED = Pin(15, Pin.OUT)
fourPlaceLED = Pin(14, Pin.OUT)
twoPlaceLED = Pin(13, Pin.OUT)
onePlaceLED = Pin(12, Pin.OUT)

# turn off all LEDs just in case any are on from last run of program
onePlaceLED.off()
twoPlaceLED.off()
fourPlaceLED.off()
eightPlaceLED.off()

while True:
    # 0000
    print("0000, 0")
    onePlaceLED.off()
    twoPlaceLED.off()
    fourPlaceLED.off()
    eightPlaceLED.off()
    sleep(delayTime)
    # 0001
    print("0001, 1")
    onePlaceLED.on()
    twoPlaceLED.off()
    fourPlaceLED.off()
    eightPlaceLED.off()
    sleep(delayTime)
    # 0010
    print("0010, 2")
    onePlaceLED.off()
    twoPlaceLED.on()
    fourPlaceLED.off()
    eightPlaceLED.off()
    sleep(delayTime)
    # 0011
    print("0011, 3")
    onePlaceLED.on()
    twoPlaceLED.on()
    fourPlaceLED.off()
    eightPlaceLED.off()
    sleep(delayTime)
    # 0100
    print("0100, 4")
    onePlaceLED.off()
    twoPlaceLED.off()
    fourPlaceLED.on()
    eightPlaceLED.off()
    sleep(delayTime)
    # 0101
    print("0101, 5")
    onePlaceLED.on()
    twoPlaceLED.off()
    fourPlaceLED.on()
    eightPlaceLED.off()
    sleep(delayTime)
    # 0110
    print("0110, 6")
    onePlaceLED.off()
    twoPlaceLED.on()
    fourPlaceLED.on()
    eightPlaceLED.off()
    sleep(delayTime)
    # 0111
    print("0111, 7")
    onePlaceLED.on()
    twoPlaceLED.on()
    fourPlaceLED.on()
    eightPlaceLED.off()
    sleep(delayTime)
    # 1000
    print("1000, 8")
    onePlaceLED.off()
    twoPlaceLED.off()
    fourPlaceLED.off()
    eightPlaceLED.on()
    sleep(delayTime)
    # 1001
    print("1001, 9")
    onePlaceLED.on()
    twoPlaceLED.off()
    fourPlaceLED.off()
    eightPlaceLED.on()
    sleep(delayTime)
    # 1010
    print("1010, 10")
    onePlaceLED.off()
    twoPlaceLED.on()
    fourPlaceLED.off()
    eightPlaceLED.on()
    sleep(delayTime)
    # 1011
    print("1011, 11")
    onePlaceLED.on()
    twoPlaceLED.on()
    fourPlaceLED.off()
    eightPlaceLED.on()
    sleep(delayTime)
    # 1100
    print("1100, 12")
    onePlaceLED.off()
    twoPlaceLED.off()
    fourPlaceLED.on()
    eightPlaceLED.on()
    sleep(delayTime)
    # 1101
    print("1101, 13")
    onePlaceLED.on()
    twoPlaceLED.off()
    fourPlaceLED.on()
    eightPlaceLED.on()
    sleep(delayTime)
    # 1110
    print("1110, 14")
    onePlaceLED.off()
    twoPlaceLED.on()
    fourPlaceLED.on()
    eightPlaceLED.on()
    sleep(delayTime)
    # 1111
    print("1111, 15")
    onePlaceLED.on()
    twoPlaceLED.on()
    fourPlaceLED.on()
    eightPlaceLED.on()
    sleep(delayTime)
    
    
    
    
    
    
    
    