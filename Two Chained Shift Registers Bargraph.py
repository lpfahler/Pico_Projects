# Two bargraphs (10 red LEDs but only use first eight)
# with network resistors (470 ohm)
#
# Beginner Version!
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

clear()
latch()

delay = 1
    
# Shift in a "1" or HIGH - move it down the bargraph #1 from QA to QH
# and bargraph #2's QA to QH


# Send in high
ser_input_pin.high()
# tick the clock to put in register
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH
#  1  0  0  0  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH = QH'
#  0  1  0  0  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH = QH'
#  0  0  1  0  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH
#  0  0  0  1  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  1  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  1  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  1  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH = QH'
#  0  0  0  0  0  0  0  1
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH = QH'
#  0  0  0  0  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  1  0  0  0  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH = QH'
#  0  0  0  0  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  1  0  0  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH = QH'
#  0  0  0  0  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  1  0  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH = QH'
#  0  0  0  0  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  1  0  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH = QH'
#  0  0  0  0  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  1  0  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH = QH'
#  0  0  0  0  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  1  0  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH = QH'
#  0  0  0  0  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  1  0
latch()

utime.sleep(delay)

# Send in low
ser_input_pin.low()
# tick the clock to put in register and shift the bits
tick()
# flip the latch - current state of the register for bargraph #1:
# QA QB QC QD QE QF QG QH = QH'
#  0  0  0  0  0  0  0  0
# bargraph #2:
# QA QB QC QD QE QF QG QH
#  0  0  0  0  0  0  0  1
latch()

utime.sleep(delay)

clear()
latch()