# Four Digit Seven Segment Display 
# Display numbers up to four digits
# Cathode type
# 330 ohm resistors for each segment
#
# Connect D1, D2, D3 ,D4 pins to GPIO 20, 21, 22, 15 respectively
#
# Lori Pfahler
# May 2025

import machine
import utime

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

# list of lists to form digits from the segments
# order is segments: a, b, c, d, e, f, g, dp 
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
    
# function for digits 0-9
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

# function to display up to a four digit number
# (no decimal points!) on led display
def display_number(number, pov_time_us = 1000, display_time_ms = 1000):
    # get the digits in the ones, tens, hundreds, and thousands place
    digit_ones = (number % 10) // 1
    digit_tens = (number % 100) // 10
    digit_hundreds = (number % 1000) // 100
    digit_thousands = (number % 10000) // 1000
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
    print(f'{number}, {count_digits}', end = '\r')
    # start the clock
    start = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start) < display_time_ms:
        for i in range(4):
            # loop through the four places D4, D3, D2, D1
            digits[i].value(0)
            display_digit(count_digits[i])
            utime.sleep_us(pov_time_us)
            digits[i].value(1)
            # set to all segments to off to avoid "carryover" to next digit
            display_digit(10)
 
# display 1234
display_number(1234, pov_time_us = 1000, display_time_ms = 5000)

try:
    # count 0 to 9999
    for i in range(10000):
        display_number(i)
    
except KeyboardInterrupt:
    # set all digits off
    for digit in digits:
        digit.value(1)
   
    
