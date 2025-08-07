# Using 4-Digit 7-Segment Display with TM1637 Driver Chip
#
# Using mcauser's library: https://github.com/mcauser/micropython-tm1637
# CLK to GPIO16
# DIO to GPIO17
# VCC to 3.3V rail
# GND Pin to GND rail
#
# Scroll characters across the display
#
# Lori Pfahler
# August 2025

import tm1637
from machine import Pin
import utime
# Setup display
tm = tm1637.TM1637(clk=Pin(16), dio=Pin(17))

# adjust brightness
tm.brightness(7)

# Siekoo Alphabet 0-9, a-z, space, dash, degree symbol(star)
SIEKOO = bytearray(b'\x3F\x06\x5B\x4F\x66\x6D\x7D\x07\x7F\x6F\x5F\x7C\x58\x5E\x79\x71\x3D\x74\x11\x0D\x75\x38\x55\x54\x5C\x73\x67\x50\x2D\x78\x1C\x2A\x6A\x14\x6E\x1B\x00\x40\x63')

try:
    while True:
        # Scroll Hello World from right to left
        tm.scroll('Hello World', 300) 
        # all LEDS off
        tm.write([0, 0, 0, 0])
        utime.sleep(2)

        tm.scroll('LORIS ROBOTS', 1000)
        # all LEDS off
        tm.write([0, 0, 0, 0])
        utime.sleep(2)

        # Scroll all available characters in library: _SEGMENTS 
        tm.scroll(list(tm1637._SEGMENTS), 300)
        # all LEDS off
        tm.write([0, 0, 0, 0])
        utime.sleep(2)
 
        # Scroll Siekoo characters : SIEKOO 
        tm.scroll(list(SIEKOO), 300)
        # all LEDS off
        tm.write([0, 0, 0, 0])
        utime.sleep(2)
        
        # Lori's Robots Using Siekoo with an apostrophe
        tm.scroll([0x38, 0x5C, 0x50, 0x11, 0x02, 0x2D, 0x00, 0x50, 0x5C, 0x7C, 0x5C, 0x78, 0x2d, 0x00] , 300)
        # all LEDS off
        tm.write([0, 0, 0, 0])
        utime.sleep(2)
        

except KeyboardInterrupt:
    # all LEDS off
    tm.write([0, 0, 0, 0])