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
                [1, 1, 1, 1, 0, 1, 1, 0],  #9
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
    print(digit, bin(digit))
    digit_selected = digit_segments[digit]
    # loop through digit_selected - put in storage register
    # go in reverse order
    for i in range(7, -1, -1):
        cur_bit = digit_selected[i]
        print(cur_bit)
        if cur_bit == 0:
            ser_input_pin.low()
        else:
            ser_input_pin.high()
        # tick the clock pin
        tick()
    # flip the latch pin
    latch()


# clear the register and enable storage register
clear()

digits[0].value(1)
digits[1].value(1)
digits[2].value(1)
digits[3].value(1)

# turn on ones place (D4)
digits[0].value(0)
# show digit for 5 seconds
display_digit(4)
utime.sleep(5)
# turn off ones place
digits[0].value(1)

# turn on tens place (D3)
digits[1].value(0)
# show digit for 5 seconds
display_digit(3)
utime.sleep(5)
# turn off tens place
digits[1].value(1)
 
# turn on hundreds place (D2)
digits[2].value(0)
# show digit for 5 seconds
display_digit(2)
utime.sleep(5)
# turn off hundreds place
digits[2].value(1)

# turn on thousands place (D1)
digits[3].value(0)
# show digit for 5 seconds
display_digit(1)
utime.sleep(5)
# turn off thousands place
digits[3].value(1)
