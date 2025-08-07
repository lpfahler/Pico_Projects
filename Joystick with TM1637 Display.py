# Using 4-Digit 7-Segment Display with TM1637 Driver Chip
# My component has decimal points but apparently they are not wired
# The colon for displaying time works
#
# Using mcauser's library: https://github.com/mcauser/micropython-tm1637
# CLK to GPIO16
# DIO to GPIO17
# VCC to 3.3V rail
# GND Pin to GND rail
#
# Use a Joystick to move around the segments for Digit 3 (right-most)
# with the display held vertically and digit 3 is at the bottom
#
#
# Lori Pfahler
# August 2025

import tm1637
from machine import Pin, ADC
import utime
# Setup display
tm = tm1637.TM1637(clk=Pin(16), dio=Pin(17))

# setup joystick
x_axis = ADC(Pin(26))
y_axis = ADC(Pin(27))

# a, b, c, d, e, f, g
segs = bytearray(b'\x01\x02\x04\x08\x10\x20\x40')

# dictionary to connect grid values to segments
digit_dict = {
    (0,2) : segs[4], (1,2) : segs[4], (2,2) : segs[5], (3,2) : segs[5], (4,2) : segs[5],
    (0,1) : segs[3], (1,1) : segs[6], (2,1) : segs[6], (3,1) : segs[6], (4,1) : segs[0],
    (0,0) : segs[2], (1,0) : segs[2], (2,0) : segs[1], (3,0) : segs[1], (4,0) : segs[1],
    }

# set initial segment location, segment g  = (2,1)
x_grid_previous = 2
y_grid_previous = 1

# clear display
tm.write([0, 0, 0, 0])

# display initial position on display
tm.write([digit_dict[(x_grid_previous, y_grid_previous)]], 3)

try:
    while True:
        # read the x and y potentiometers
        x_value = x_axis.read_u16()
        y_value = y_axis.read_u16()
        
        # determine the x grid location - make equally spaced intervals
        if x_value <= 13107:
            x_grid = 0
        elif x_value <= 26214:
            x_grid = 1
        elif x_value <= 39321:
            x_grid = 2
        elif x_value <= 54428:
            x_grid = 3
        else:
            x_grid = 4
        # determine the y grid location - make equally spaced intervals   
        if y_value <= 21845:
            y_grid = 0
        elif y_value <= 43690:
            y_grid = 1
        else:
            y_grid = 2
                  
        # update segment illuminated only if grid values have changed
        if x_grid != x_grid_previous or y_grid != y_grid_previous:
            # clear display
            tm.write([0], 3)
        
            # update to new segment
            tm.write([digit_dict[(x_grid, y_grid)]], 3)        
            print(f'X: {x_value:5d}, x_grid: {x_grid:1d}, Y: {y_value:5d} y_grid: {y_grid:1d}')
            
            # update previous grid values
            x_grid_previous = x_grid
            y_grid_previous = y_grid
        
        utime.sleep(0.1)

except KeyboardInterrupt:
    # clear display
    tm.write([0, 0, 0, 0])