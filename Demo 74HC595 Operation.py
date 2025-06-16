# Bargraph (10 red LEDs) using network resistors (470 ohm)
# and 74HC595 IC shift register for control of
# eight of the LEDs on the bargraph
#
# Demostrate how the shift register works
#
# functions adapted from Kevin McAleer:
#     https://www.youtube.com/live/iSTlP4Lbibs?si=NUKTNka81qMmFrw- 
#
# Lori Pfahler
# June 2025

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

clear()
latch()
    
# Shift in a "1" or HIGH - move it down the bargraph from QA to QH:


# Send in high
ser_input_pin.high()
# tick the clock to put in register
tick()
# flip the latch - current state of the register:
# QA QB QC QD QE QF QG QH
#  1  0  0  0  0  0  0  0
latch()

utime.sleep(1)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register:
# QA QB QC QD QE QF QG QH
#  0  1  0  0  0  0  0  0
latch()

utime.sleep(1)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register:
# QA QB QC QD QE QF QG QH
#  0  0  1  0  0  0  0  0
latch()

utime.sleep(1)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register:
# QA QB QC QD QE QF QG QH
#  0  0  0  1  0  0  0  0
latch()

utime.sleep(1)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  1  0  0  0
latch()

utime.sleep(1)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  1  0  0
latch()

utime.sleep(1)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  1  0
latch()

utime.sleep(1)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  0  1
latch()

utime.sleep(1)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  0  0
latch()

utime.sleep(1)
