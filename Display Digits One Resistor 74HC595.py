# Seven Segment Display using one resistor on GND pin
# use persistance of vision; quickly turn segments for digit on and off
# Display Digits 0-9
# Connect cathode pin to ground rail with a resistor
#
# Lori Pfahler
# April 2025

import machine
import utime

# list of binary numbers form digits from the segments
# order is segments: a, b, c, d, e, f, g, dp 
digit_segments =[
                0b11111100, #0
                0b01100000, #1
                0b11011010, #2
                0b11110010, #3
                0b01100110, #4
                0b10110110, #5
                0b10111110, #6
                0b11100000, #7
                0b11111110, #8
                0b11110110  #9    
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
    digit_bin = digit_segments[digit]
    # control the time that the digit is on with while loop
    start = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start) < display_time:
        # loop through digit_bin
        for i in range(8):
            # get just the value at position i
            # light position i only - fill storage register
            # with zeros for all other segments
            cur_value = digit_bin & (2**i)
            for j in range(8):
                cur_bit = cur_value >> j & 1
                if cur_bit == 0:
                    ser_input_pin.low()
                else:
                    ser_input_pin.high()
                # tick the clock pin
                tick()
            # flip the latch pin and wait a very short time
            # for just that segment to be visible
            latch()
            utime.sleep_us(1000)
            # move to the next segment in the digit


# clear the register and enable storage register
clear()
 
# count up
for i in range(10):
    write_digit(i, display_time = 1000)

# clear the register and flip the latch
clear()
latch()
    






