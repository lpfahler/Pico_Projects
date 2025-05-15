# Seven Segment Display using one resistor on GND pin
# use persistance of vision; quickly turn segments for digit on and off
# Display Digits 0-9
# Connect cathode pin to ground rail with a resistor
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
def display_char(digit, display_time = 500):
    digit_list = digit_segments[digit]
    start = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start) < display_time:
        for i in range(8):
            # turn segment on and off as fast as possible
            # (if that segment is needed for the digit)
            segments[i].value(digit_list[i])
            # you can adjust this value to see when the POV starts to "fall apart"
            utime.sleep_us(2500)
            segments[i].value(0)



# function to turn off all segments
def display_clear():
    for i in range(8):
        segments[i].value(0)
            
# delay times
delay_ms = 500
delay_long = 1


try: 
    while True:
        # turn on the segments to count from 0 to 9
        for i in range(10):
            display_char(i, display_time = delay_ms)
            
        # clear display
        display_clear()
        utime.sleep(delay_long)
        
        # turn on the segments to count from 9 to 0
        for i in range(9, -1, -1):
            display_char(i, display_time = delay_ms)


        # clear display
        display_clear()
        utime.sleep(delay_long)
        
except KeyboardInterrupt:
    # turn off all segments
    display_clear()



