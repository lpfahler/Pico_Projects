# Two bargraphs (10 red LEDs but only use first eight)
# with network resistors (470 ohm)
#
# Use two "chained" 74HC595 shift registers for control of
# first eight LEDs on the bargraph #1 and
# first eight LEDS on bargraph #2
#
# Write 16 bits at a time - make some fun patterns
# Write the value to turn every other LED in both bargraphs
# LED Chaser Example
#
# Lori Pfahler
# July 2025

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

# write binary number to the two shift registers - 16 bits
def write_num(value):
    for i in range(16):
        cur_bit = value >> i & 1
        if cur_bit == 0:
            ser_input_pin.low()
        else:
            ser_input_pin.high()
        # tick the clock pin
        tick()
    # flip the latch pin
    latch()


# clear the register and make sure the LEDs are off
clear()
latch()

# timing
delay = 0.075

try:
    while True:
        for i in range(15, -1, -1):
            write_num(2**i)
            utime.sleep(delay)            
        for j in range(1, 14):
            write_num(2**j)
            utime.sleep(delay)

except KeyboardInterrupt:
    clear()
    latch()

