# Four Digit Seven Segment Display Basic Code
# Cathode type
# 330 ohm resistors for each segment
#
# Connect pins for segments a, b, c, d, e, f, g, dp
# to GPIO 6, 7, 8, 9, 10, 11, 12, 13 respectively
#
# Connect D1, D2, D3 ,D4 pins to GPIO 16, 17, 18, 19 respectively
#
# Lori Pfahler
# May 2025

import machine
import utime

# Set up segments
a_LED = machine.Pin(6, machine.Pin.OUT) 
b_LED = machine.Pin(7, machine.Pin.OUT)  
c_LED = machine.Pin(8, machine.Pin.OUT)  
d_LED = machine.Pin(9, machine.Pin.OUT)  
e_LED = machine.Pin(10, machine.Pin.OUT)  
f_LED = machine.Pin(11, machine.Pin.OUT)  
g_LED = machine.Pin(12, machine.Pin.OUT)  
dp_LED = machine.Pin(13, machine.Pin.OUT)

# Set up Control Pins for Digits
D1 = machine.Pin(16, machine.Pin.OUT)
D2 = machine.Pin(17, machine.Pin.OUT)
D3 = machine.Pin(18, machine.Pin.OUT)
D4 = machine.Pin(15, machine.Pin.OUT)

# lists in order for looping - top to bottom
segments_order = [a_LED, f_LED, b_LED, g_LED, e_LED, c_LED, d_LED, dp_LED]
digits = [D1, D2, D3, D4]

# set all digits off - use value = 1 for cathode; 0 for anode
for digit in digits:
    digit.value(1)
# set all segments off - can be carryover from last run
for segment in segments_order:
    segment.value(0)
    
# set up delay times in seconds
delay_short = 0.1
delay_long = 0.5

try: 
    while True:
        # Loop through each digit
        for digit in digits:
            # turn on digit use value of 0 for cathode; 1 for anode
            digit.value(0)
            # turn on the segments - top to bottom
            for segment in segments_order:
                segment.value(1)
                utime.sleep(delay_short)
                
            utime.sleep(delay_long) 
            
            # turn off the segments bottom to top
            for segment in reversed(segments_order):
                segment.value(0)
                utime.sleep(delay_short)
                
            utime.sleep(delay_long)
            # turn off digit
            digit.value(1)

except KeyboardInterrupt:
    # set all digits off
    for digit in digits:
        digit.value(1)
    # set all segments off
    for segment in segments_order:
        segment.value(0)







