# Seven Segment Display using eight resistors on GND pin
# Display Digits 0-9
# Use eight resistors - one per segment
#
# Lori Pfahler
# April 2025

import machine
import utime

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
                [1, 1, 1, 1, 0, 1, 1, 0]  #9    
                ]

# Set up shift register control pins            
ser_input_pin  = machine.Pin(16, machine.Pin.OUT) 
latch_pin = machine.Pin(17, machine.Pin.OUT) 
clock_pin = machine.Pin(18, machine.Pin.OUT) 
clear_reg_pin = machine.Pin(19, machine.Pin.OUT)

# set the pins to low
ser_input_pin.low()
latch_pin.low()
clock_pin.low()

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
    
    
def write_digit(digit, display_time = 1000):
    digit_selected = digit_segments[digit]
    # control the time that the digit is on
    start = utime.ticks_ms()
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
    while utime.ticks_diff(utime.ticks_ms(), start) < display_time:
        pass



# clear the register and enable storage register
clear()
 
# count up
for i in range(10):
    write_digit(i, display_time = 1000)

# clear the register and flip the latch
clear()
latch()
    







