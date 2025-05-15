# Bargraph (10 red LEDs) using network resistors (470 ohm)
# and 74HC595 IC shift register for control of
# eight of the LEDs on the bargraph
#
# Binary Counter
#
# Lori Pfahler
# April 2025

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

# write binary number to the shift register
# value can be in binary or decimal format
def write_num(value):
    print(bin(value), value)
    for i in range(8):
        cur_bit = value >> i & 1
        # print("current bit is", cur_bit)
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

# binary counter 0 to 255
try:
    while True:
        for i in range(256):
            write_num(i)
            utime.sleep(0.5)

except KeyboardInterrupt:
    # clear the register and make sure the LEDs are off
    clear()
    latch()    
    







