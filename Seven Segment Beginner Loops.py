# Seven Segment Display Beginner Code
# Using for Lists, Loops and "try-except" code
# Light up each segment and then turn each off - top to bottom
# 220 ohm resistors for each segment
# Connect cathode pins to ground rail
#
# Lori Pfahler
# April 2025

import machine
import utime

# Set up segments
a_LED = machine.Pin(13, machine.Pin.OUT) 
b_LED = machine.Pin(12, machine.Pin.OUT)  
c_LED = machine.Pin(18, machine.Pin.OUT)  
d_LED = machine.Pin(19, machine.Pin.OUT)  
e_LED = machine.Pin(16, machine.Pin.OUT)  
f_LED = machine.Pin(14, machine.Pin.OUT)  
g_LED = machine.Pin(15, machine.Pin.OUT)  
dp_LED = machine.Pin(17, machine.Pin.OUT)  

# lists in order for looping
segments_topdown = [a_LED, f_LED, b_LED, g_LED, e_LED, c_LED, d_LED, dp_LED]
segments_bottomup = [dp_LED, d_LED, c_LED, e_LED, g_LED, b_LED, f_LED, a_LED]

# set up delay times
delay_short = 0.1
delay_long = 1

try: 
    while True:
        # turn on the segments - top to bottom
        for segment in segments_topdown:
            segment.value(1)
            utime.sleep(delay_short)
            
        utime.sleep(delay_long) 
        
        # turn off the segments bottom to top
        for segment in segments_bottomup:
            segment.value(0)
            utime.sleep(delay_short)
            
        utime.sleep(delay_long)

except KeyboardInterrupt:
    # turn off all setments
        for segment in segments_topdown:
            segment.value(0)


