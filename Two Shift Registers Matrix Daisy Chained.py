# Two Shift Registers Daisy Chained to Control an 8x8 LED Matrix
# First Program - light every other LED by row
#
# Common Anode "788BS"
# 470 ohm resistor array on columns (cathodes)
# Row 1 is connected to QA ... Row 8 to QH on second shift register
# Col 1 is connected to QA ... Col 8 to QH on first shift register
#
# Lori Pfahler
# July 2025

import machine
import utime

# Set up shift register control pins
ser_input = machine.Pin(15, machine.Pin.OUT)
latch_pin = machine.Pin(17, machine.Pin.OUT) 
clock_pin = machine.Pin(16, machine.Pin.OUT) 
clear_reg_pin = machine.Pin(18, machine.Pin.OUT)

# set the pins to low/high for off setting
ser_input.low()
latch_pin.low()
clock_pin.low()
clear_reg_pin.high()

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
    
# Input the row and col settings to the shift registers together
def row_col_write(row_val, col_val):
    # input row settings first - row shift register is second
    for i in range(8):
        row_bit = row_val >> i & 1
        if row_bit == 0:
            ser_input.low()
        else:
            ser_input.high()
        tick()
    # input column settings second - column shift register is first
    for i in range(8):            
        col_bit = col_val >> i & 1
        # using common anode display
        if col_bit == 0:
            ser_input.high() 
        else:
            ser_input.low()
        # tick the clock pin
        tick()
    # flip the latch pin
    latch()


delay = 0.2
clear()
latch()

try:
    while True:
        for i in range(7, -1, -1):
            row_col_write(row_val = 2**i, col_val = 0b10101010)
            utime.sleep(delay)
            row_col_write(row_val = 2**i, col_val = 0b01010101)
            utime.sleep(delay)   

except KeyboardInterrupt:
    clear()
    latch()


