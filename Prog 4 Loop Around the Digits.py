# Using 4-Digit 7-Segment Display with TM1637 Driver Chip
#
# Using mcauser's library: https://github.com/mcauser/micropython-tm1637
# CLK to GPIO16
# DIO to GPIO17
# VCC to 3.3V rail
# GND Pin to GND rail
#
# Spin around the digits!
#
# Lori Pfahler
# August 2025

import tm1637
from machine import Pin
import utime
# Setup display
tm = tm1637.TM1637(clk=Pin(16), dio=Pin(17))

# create path by turning on individual segments - "loop the zero"
# segments: a, b, c, d, e, f
# leave segment a on
path_segments_1 = list(bytearray(b'\x01\x02\x04\x08\x10\x20\x01'))
# leave no LEDs on
path_segments_2 = list(bytearray(b'\x01\x02\x04\x08\x10\x20\x01\x00'))


# clear display
tm.write([0, 0, 0, 0])

# speed of looping
delay = 0.1

try:
    while True:
        # loop through digits #0 is left-most digit, #3 is right-most digit
        for i in range(4):
            # loop through path_segments
            for num in path_segments_1:
                tm.write([num], i)
                utime.sleep(delay)
        # clear display
        tm.write([0, 0, 0, 0])
        # loop through digits #0 is left-most digit, #3 is right-most digit
        for i in range(4):
            # loop through path_segments
            for num in path_segments_2:
                tm.write([num], i)
                utime.sleep(delay)


except KeyboardInterrupt:
    # clear display
    tm.write([0, 0, 0, 0])
