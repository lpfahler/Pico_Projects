# Find Decimal Point 
#
# Lori Pfahler
# May 2025

import machine
import utime
from math import log10, floor

# Set up shift register control pins            
ser_input_pin  = machine.Pin(16, machine.Pin.OUT) 
latch_pin = machine.Pin(17, machine.Pin.OUT) 
clock_pin = machine.Pin(18, machine.Pin.OUT) 
clear_reg_pin = machine.Pin(19, machine.Pin.OUT)

# set the pins to low
ser_input_pin.low()
latch_pin.low()
clock_pin.low()

# Set up Control Pins for Digits
D1 = machine.Pin(20, machine.Pin.OUT)
D2 = machine.Pin(21, machine.Pin.OUT)
D3 = machine.Pin(22, machine.Pin.OUT)
D4 = machine.Pin(15, machine.Pin.OUT)

# dictionary to form digits from the segments
# order is segments: a, b, c, d, e, f, g, dp
digit_segments = {
                '0'     : [1, 1, 1, 1, 1, 1, 0, 0],
                '1'     : [0, 1, 1, 0, 0, 0, 0, 0],
                '2'     : [1, 1, 0, 1, 1, 0, 1, 0],
                '3'     : [1, 1, 1, 1, 0, 0, 1, 0], 
                '4'     : [0, 1, 1, 0, 0, 1, 1, 0], 
                '5'     : [1, 0, 1, 1, 0, 1, 1, 0], 
                '6'     : [1, 0, 1, 1, 1, 1, 1, 0], 
                '7'     : [1, 1, 1, 0, 0, 0, 0, 0], 
                '8'     : [1, 1, 1, 1, 1, 1, 1, 0], 
                '9'     : [1, 1, 1, 1, 0, 1, 1, 0], 
                '0dp'   : [1, 1, 1, 1, 1, 1, 0, 1], 
                '1dp'   : [0, 1, 1, 0, 0, 0, 0, 1], 
                '2dp'   : [1, 1, 0, 1, 1, 0, 1, 1],
                '3dp'   : [1, 1, 1, 1, 0, 0, 1, 1], 
                '4dp'   : [0, 1, 1, 0, 0, 1, 1, 1], 
                '5dp'   : [1, 0, 1, 1, 0, 1, 1, 1], 
                '6dp'   : [1, 0, 1, 1, 1, 1, 1, 1],
                '7dp'   : [1, 1, 1, 0, 0, 0, 0, 1],
                '8dp'   : [1, 1, 1, 1, 1, 1, 1, 1],
                '9dp'   : [1, 1, 1, 1, 0, 1, 1, 1],
                'dp'    : [0, 0, 0, 0, 0, 0, 0, 1],
                'blank' : [0, 0, 0, 0, 0, 0, 0, 0],
                'OOR'   : [0, 0, 0, 0, 0, 0, 1, 0], # OOR = out of range, place a dash
                }

# in "reverse" order since D4 is ones place -- D1 is thousands place
digits = [D4, D3, D2, D1]

# functions for shift register operation:

# clear the shift register
def clear():
    clear_reg_pin.low()
    clear_reg_pin.high()

# tick the clock pin
def tick():
    clock_pin.low()
    clock_pin.high()

# flip the latch pin
def latch():
    latch_pin.high()
    latch_pin.low()
    
# function for digits 0-9, 0-9 with decimal point, blank
def display_digit(digit):
    digit_selected = digit_segments[digit]
    # loop through digit_selected - put in storage register
    # go in reverse order
    for i in range(7, -1, -1):
        cur_bit = digit_selected[i]
        if cur_bit == 0:
            ser_input_pin.low()
        else:
            ser_input_pin.high()
        # tick the clock pin
        tick()
    # flip the latch pin
    latch()
    
# function to find index of decimal point(dp)
# will return index value for dp or -1 if dp not present
def find_dp(num_str):
    dp_loc = num_str.find('.')
    return dp_loc

# function to remove decimal point
def remove_dp(num_str):
    new_str = num_str.replace('.', '')
    return new_str

# function to round to a specified number of significant digits
# https://stackoverflow.com/questions/3410976/how-to-round-a-number-to-significant-figures-in-python
def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)

# display a four digit number of the display
def display_number(number, pov_time_us = 1000, display_time_ms = 1000):
    # round number to four significant digits
    number = round_sig(number, sig = 4)
    
    # make a string version of number with two decimal places
    number_str = f'{number:05.2f}'
    # print(number_str)
    
    # find index of dp if present
    dp_index = find_dp(number_str)
    # print(dp_index)
    
    # remove dp if needed
    if dp_index >= 0:
        number_str = remove_dp(number_str)
    # print(number_str)
    
    # if number is greater that 1000 or less that 0.01,
    # put four dashes on display to indicate Out Of Range (OOR)
    if number > 1000 or number < 0.01:
        count_digits = ['OOR', 'OOR', 'OOR', 'OOR']
    else:
        # if number has more than 4 digits
        # drop the digits after the first 4 digits
        if len(number_str) > 4:
            number_str = number_str[0:4]
        # print(number_str) 
        # get the digits individually
        digit4 = number_str[3]
        digit3 = number_str[2]
        digit2 = number_str[1]
        digit1 = number_str[0]
        # add in decimal point at approprite digit if needed
        if dp_index == 0:
            digit1 = '0dp'
            digit2 = digit1
            digit3 = digit2
            digit4 = digit3
        if dp_index == 1:
            digit1 = digit1 + 'dp'
        if dp_index == 2:
            digit2 = digit2 + 'dp'
        if dp_index == 3:
            digit3 = digit3 + 'dp'
        # make a list of the digits to facilitate for loop below
        count_digits = [digit4, digit3, digit2, digit1]

    # start the clock
    start = utime.ticks_ms()
    
    # send data to display
    while utime.ticks_diff(utime.ticks_ms(), start) < display_time_ms:
        for i in range(4):
            # loop through the four places D4, D3, D2, D1
            digits[i].value(0)
            display_digit(count_digits[i])
            utime.sleep_us(pov_time_us)
            digits[i].value(1)
            # set to all segments to off to avoid "carryover" to next digit
            display_digit('blank')   

# testing 
display_number(0.123, pov_time_us = 1000, display_time_ms = 5000)
utime.sleep(1)

display_number(12.34, pov_time_us = 1000, display_time_ms = 5000)
utime.sleep(1)

display_number(123.4, pov_time_us = 1000, display_time_ms = 5000)
utime.sleep(1)

display_number(1234, pov_time_us = 1000, display_time_ms = 5000)
utime.sleep(1)

display_number(100.19, pov_time_us = 1000, display_time_ms = 5000)
utime.sleep(1)

display_number(58.9, pov_time_us = 1000, display_time_ms = 5000)
utime.sleep(1)

display_number(1005.8, pov_time_us = 1000, display_time_ms = 5000)
utime.sleep(1)

display_number(0.001, pov_time_us = 1000, display_time_ms = 5000)


