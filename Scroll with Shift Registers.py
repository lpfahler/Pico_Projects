# Two Shift Registers Daisy Chained to Control an 8x8 LED Matrix
# Scroll Graphics
# Common Anode "788BS"
# 470 ohm resistor array on columns (cathodes)
# Row 1 is connected to QA ... Row 8 to QH on second shift register
# Col 1 is connected to QA ... Col 8 to QH on first shift register
# Use persistance of vision to display graphics - quickly moving through the rows
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


# function to display an 8x8 graphic or character
def display_graphic(graphic, pov_time_us = 1000, display_time_ms = 1000):
    start = utime.ticks_ms()
    # display graphic
    while utime.ticks_diff(utime.ticks_ms(), start) < display_time_ms:
        for i in range(7, -1, -1):
            row_col_write(row_val = 2**i, col_val = graphic[7-i])
            utime.sleep_us(pov_time_us)  

# graphics to display
note = [0b00000000,
        0b00011000,
        0b00010100,
        0b00010000,
        0b00010000,
        0b00110000,
        0b01110000,
        0b01100000]

tree = [0b00000000,
        0b00001000,
        0b00011100,
        0b00111110,
        0b01111111,
        0b00111110,
        0b00001000,
        0b00011100]

house = [0b00000000,
         0b00001000,
         0b00011100,
         0b00110110,
         0b01100011,
         0b01000001,
         0b01000001,
         0b01111111]

blank = [0b00000000,
         0b00000000,
         0b00000000,
         0b00000000,
         0b00000000,
         0b00000000,
         0b00000000,
         0b00000000]

message = [blank, note, tree, house, blank]

# function to create new graphic that is comprised of two graphics
# shifted to the left for scrolling effect
def window(graphic1, graphic2, shift = 1):
    new_graphic = []
    # create new graphic row by row according the shift requested
    for i in range(8):
        # make two strings needed from each graphic from binary values
        graph1_str = f'{graphic1[i]:>08b}'[shift:8]
        graph2_str = f'{graphic2[i]:>08b}'[0:shift]
        # make new row by concatenating the strings and then converting to binary number
        new_row = int(graph1_str + graph2_str, 2)
        # append new row to the combined graphic list
        new_graphic.append(new_row)
    return new_graphic


try:
    clear()
    latch()
    while True:
    # loop through message
        for i in range(len(message) - 1):
            # shift the letters off the display one column at a time
            for j in range(8):
                new_character = window(message[i], message[i+1], shift = j)
                display_graphic(new_character, 1000, 60)
        # short delay to signal message is starting over
        clear()
        latch()
        utime.sleep(1)

except KeyboardInterrupt:
    clear()
    latch()


