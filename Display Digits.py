# Seven Segment Display
# Display Digits 0-9
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

# list for segments
segments = [a_LED, b_LED, c_LED, d_LED, e_LED, f_LED, g_LED, dp_LED]

# list of lists to form digits from the segments
digit_segments =[
                [1, 1, 1, 1, 1, 1, 0, 0], #0
                [0, 1, 1, 0, 0, 0, 0, 0], #1
                [1, 1, 0, 1, 1, 0, 1, 0], #2
                [1, 1, 1, 1, 0, 0, 1, 0], #3
                [0, 1, 1, 0, 0, 1, 1, 0], #4
                [1, 0, 1, 1, 0, 1, 1, 0], #5
                [1, 0, 1, 1, 1, 1, 1, 0], #6
                [1, 1, 1, 0, 0, 0, 0, 0], #7
                [1, 1, 1, 1, 1, 1, 1, 0], #8
                [1, 1, 1, 1, 0, 1, 1, 0]  #9    
                ]

# function for digits 0-9
def display_char(digit):
    digit_list = digit_segments[digit]
    for i in range(8):
        segments[i].value(digit_list[i])

# function to turn off all segments
def display_clear():
    for i in range(8):
        segments[i].value(0)
            
# delay time
delay = 0.5


try: 
    while True:
        # turn on the segments to count from 0 to 9
        for i in range(10):
            display_char(i)
            utime.sleep(delay)
            
        # clear display
        display_clear()
        utime.sleep(delay)
        
        # turn on the segments to count from 9 to 0
        for i in range(9, -1, -1):
            display_char(i)
            utime.sleep(delay)

        # clear display
        display_clear()
        utime.sleep(delay)
        
except KeyboardInterrupt:
    # turn off all segments
    display_clear()


