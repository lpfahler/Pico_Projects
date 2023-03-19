# Program to read the two potentiometers for Etch-A-Sketch Project
# Lori Pfahler
# March 2023
# Output from read_potentiometers_calibrate.py
# Green Low Average = 417.6
# Blue Low Average = 419.2 
#
# Green High Average = 65517.4
# Blue High Average = 65472.6

# import modules
import machine
from utime import sleep

# setup potentiometers on ADC pins: ADC0 and ADC1
bluePot = machine.ADC(26)
greenPot = machine.ADC(27)

# function to scale x to y based on range of x and y
def scale(value, xmin, xmax, ymin, ymax):
    slope = (ymax - ymin)/(xmax - xmin)
    scaled_value = slope * (value - xmin) + ymin
    return(scaled_value)

while True:
    # read potentiometers
    blueValue = bluePot.read_u16()
    greenValue = greenPot.read_u16()
    # green has a min of 417 - scale to 4 to 123) to give a
    # border of four pixels - call this xpos
    xpos = int(scale(greenValue, 418, 65517, 4, 123))
    # blue has a min of ~500 - scale to 3, 61 to give a border
    # of three pixels to screen - call this ypos
    ypos = int(scale(blueValue, 419, 65473, 3, 61))
    # print values to shell
    print('Green Pot = xpos: ', greenValue, '=', xpos) 
    print('Blue Pot = ypos:  ', blueValue, '=', ypos, '\n')
    sleep(1)
    
