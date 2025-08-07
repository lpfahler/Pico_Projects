# Using 4-Digit 7-Segment Display with TM1637 Driver Chip
#
# Using mcauser's library: https://github.com/mcauser/micropython-tm1637
# CLK to GPIO16
# DIO to GPIO17
# VCC to 3.3V rail
# GND Pin to GND rail
#
# Turn on all LEDS and show temperature
#
# Lori Pfahler
# August 2025

import tm1637
from machine import Pin
import utime
# Setup display
tm = tm1637.TM1637(clk=Pin(16), dio=Pin(17))

# adjust brightness
tm.brightness(3)

try:
    while True:        
        # all LEDS on "88:88"
        # Numerous approaches:
        # tm.write([127, 255, 127, 127])
        # tm.write(bytearray([127, 255, 127, 127]))
        # tm.write(b'\x7F\xFF\x7F\x7F')
        # tm.show('8888', True)
        tm.numbers(88, 88, True)
        utime.sleep(2)
        
        # all LEDS off
        tm.write([0, 0, 0, 0])
        # tm.show('    ')
        utime.sleep(1)
        
        # show temperature in Celcius for range -9 to +99
        tm.temperature(-10) # LO*C
        utime.sleep(2)
        tm.temperature(-9)  # -9*C
        utime.sleep(2)
        tm.temperature(5)   #  5*C
        utime.sleep(2)
        tm.temperature(99)  # 99*C
        utime.sleep(2)
        tm.temperature(100) # HI*C
        utime.sleep(2)
        
        

except KeyboardInterrupt:
    # all LEDS off
    tm.write([0, 0, 0, 0])
