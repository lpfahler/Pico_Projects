# Four Digit Seven Segment Display Count from 0 to 9999
# Eliminate Leading Zeros
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

segments = [a_LED, b_LED, c_LED, d_LED, e_LED, f_LED, g_LED, dp_LED]
# in "reverse" order since D4 is ones place -- D1 is thousands place
digits = [D4, D3, D2, D1]

# list of lists to form digits from the segments
# digit_segments[10] is all segments off - blank
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
                [1, 1, 1, 1, 0, 1, 1, 0], #9
                [0, 0, 0, 0, 0, 0, 0, 0], #Blank
                ]

# function for digits 0-9
def display_digit(digit):
    digit_list = digit_segments[digit]
    for i in range(8):
        segments[i].value(digit_list[i])

# delay in microseconds (timing for POV); display_time in milliseconds
delay = 1000
display_time = 500

# set all digits off - use value = 1 for cathode; 0 for anode
for digit in digits:
    digit.value(1)
# set all segments off - can be carryover from last run
for segment in segments:
    segment.value(0)
    
try:        
    while True:
        for i in range(10000):
            # get the digits in the ones, tens, hundreds, and thousands place
            digit_ones = (i % 10) // 1
            digit_tens = (i % 100) // 10
            digit_hundreds = (i % 1000) // 100
            digit_thousands = (i % 10000) // 1000
            # clear out leading zeros so they do not show on display
            if digit_thousands == 0:
                # setting to 10 means the character/digit displayed will be "blank"
                digit_thousands = 10
                if digit_hundreds == 0:
                    digit_hundreds = 10
                    if digit_tens == 0:
                        digit_tens = 10
            # make a list of the digits to facilitate for loop below
            count_digits = [digit_ones, digit_tens, digit_hundreds, digit_thousands]
            # show count for the display time
            start = utime.ticks_ms()
            while utime.ticks_diff(utime.ticks_ms(), start) < display_time:
                for i in range(4):
                    # loop through the four places D4, D3, D2, D1
                    digits[i].value(0)
                    display_digit(count_digits[i])
                    utime.sleep_us(delay)
                    digits[i].value(1)
                    # set to all segments to off to avoid "carryover" to next digit
                    display_digit(10)

except KeyboardInterrupt:
    # set all digits off
    for digit in digits:
        digit.value(1)
    # set all segments off
    for segment in segments:
        segment.value(0)