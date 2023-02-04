# Program to blink "SOS" using Morse Code on an LED
# Lori Pfahler
# Feb 2023

# import libraries
from machine import Pin
from utime import sleep

# setup LED
redLED = Pin(15, Pin.OUT)

# create needed sleep times:
#   10 words per minute: dot = 0.12 seconds
#   5 words per minute: dot = 0.24 seconds
dot = 0.24
dash = 3 * dot
withinChar = dot
betChar = 3 * dot
# betWord = 7 * dot

# make sure LED is off
redLED.value(0)

while True:
    #Blink SOS
    print('Sending SOS in 2 seconds')
    sleep(2)
    # S = ...
    print('S = ...')
    redLED.value(1)
    sleep(dot)
    redLED.value(0)
    sleep(withinChar)
    redLED.on()
    sleep(dot)
    redLED.off()
    sleep(withinChar)
    redLED.on()
    sleep(dot)
    redLED.off()
    sleep(betChar)
    # O = ---
    print('O = ---')
    redLED.on()
    sleep(dash)
    redLED.off()
    sleep(withinChar)
    redLED.on()
    sleep(dash)
    redLED.off()
    sleep(withinChar)
    redLED.on()
    sleep(dash)
    redLED.off()
    sleep(betChar)
    # S = ...
    print('S = ...')    
    redLED.on()
    sleep(dot)
    redLED.off()
    sleep(withinChar)
    redLED.on()
    sleep(dot)
    redLED.off()
    sleep(withinChar)
    redLED.on()
    sleep(dot)
    redLED.off()
    sleep(betChar)
    print('Repeating ...')
    