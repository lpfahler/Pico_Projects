# Two bargraphs (10 red LEDs but only use first eight)
# with network resistors (470 ohm)
#
# Streamlined Version!
#
# Use two "chained" 74HC595 shift registers for control of
# first eight LEDs on the bargraph #1 and
# first eight LEDS on bargraph #2
#
# Demostrate how the shift registers chain together
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
    
# speed of LED lighting
delay = 0.05
    
# Shift in a "1" or HIGH - move it down the bargraph #1 from QA to QH
# and bargraph #2's QA to QH - and repeat.

try:
    while True:
        clear()
        latch()
        # send in "1" to the register
        ser_input_pin.high()
        tick()
        latch()
        utime.sleep(delay)
        # shift the "1" down register for both bargraph #1 and #2
        for i in range(15):
            ser_input_pin.low()
            tick()
            latch()
            utime.sleep(delay)

except KeyboardInterrupt:
    clear()
    latch()
