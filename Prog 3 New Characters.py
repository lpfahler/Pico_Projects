# Using 4-Digit 7-Segment Display with TM1637 Driver Chip
#
# Using mcauser's library: https://github.com/mcauser/micropython-tm1637
# CLK to GPIO16
# DIO to GPIO17
# VCC to 3.3V rail
# GND Pin to GND rail
#
# Create some new characters
#
# Lori Pfahler
# August 2025

import tm1637
from machine import Pin
import utime
# Setup display
tm = tm1637.TM1637(clk=Pin(16), dio=Pin(17))

# clear display
tm.write([0, 0, 0, 0])
    
# Lower half circle - kind of like a period
# here I use binary to indicate the segments that I want on:
# h g f e d c b a
# 0 1 0 1 1 1 0 0
tm.write([0b01011100], 3)
utime.sleep(2)

# vertical LEDs
tm.write([0b00110110], 3)
utime.sleep(2)

# horizontal LEDs
tm.write([0b01001001], 3)
utime.sleep(2)


# loop through vertical and horizontal
for i in range(20):
    # vertical LEDs
    tm.write([0b00110110], 3)
    utime.sleep(0.25)
    # horizontal LEDs
    tm.write([0b01001001], 3)
    utime.sleep(0.25)

# clear display
tm.write([0, 0, 0, 0])
