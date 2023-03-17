# Program to read the two potentiometers to see range
# Lori Pfahler
# March 2023

# import modules
import machine
from utime import sleep

# setup potentiometers on ADC pins: ADC0 and ADC1
bluePot = machine.ADC(26)
greenPot = machine.ADC(27)

while True:
    # read potentiometers
    blueValue = bluePot.read_u16()
    greenValue = greenPot.read_u16()
    print('Green Pot = ', greenValue)
    print('Blue Pot = ', blueValue)
    sleep(1)