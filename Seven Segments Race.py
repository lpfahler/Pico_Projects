# Seven Segment Display Race Around Figure Eight
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

# list in order for looping
segments_race = [a_LED, f_LED, g_LED, c_LED, d_LED, e_LED, g_LED, b_LED]

# set up delay time
delay = 0.1


try: 
    while True:
        # turn on the segments - race
        for segment in segments_race:
            segment.value(1)
            utime.sleep(delay)
            segment.value(0)

except KeyboardInterrupt:
    # turn off all setments
        for segment in segments_race:
            segment.value(0)



