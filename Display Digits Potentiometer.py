# Seven Segment Display using one resistor on GND pin
# use persistance of vision; quickly turn segments for digit on and off
# Display Digits 0-9
# Connect cathode pin to ground rail with a resistor
# Use potentiometer to control scanning speed
#
# Lori Pfahler
# April 2025

import machine
import utime

# Set up segments
a_LED = machine.Pin(13, machine.Pin.OUT) 
b_LED = machine.Pin(12, machine.Pin.OUT)  
c_LED = machine.Pin(18, machine.Pin.OUT)  
d_LED = machine.Pin(19, machine.Pin.OUT)  
e_LED = machine.Pin(16, machine.Pin.OUT)  
f_LED = machine.Pin(14, machine.Pin.OUT)  
g_LED = machine.Pin(15, machine.Pin.OUT)  
dp_LED = machine.Pin(17, machine.Pin.OUT)  

# list for segments
segments = [a_LED, b_LED, c_LED, d_LED, e_LED, f_LED, g_LED, dp_LED]

# list of lists to form digits from the segments
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
                [1, 1, 1, 1, 0, 1, 1, 0]  #9    
                ]

# set up potentiometer on ADC0, GPIO pin 26
pot = machine.ADC(26)

# function to scale x to y based on range of x and y
def scale(value, xmin, xmax, ymin, ymax):
    slope = (ymax - ymin)/(xmax - xmin)
    scaled_value = slope * (value - xmin) + ymin
    return scaled_value

# function for digits 0-9
def display_char(digit, display_time = 500, scan_speed = 100):
    digit_list = digit_segments[digit]
    start = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start) < display_time:
        for i in range(8):
            # turn segment on and off as fast as possible
            # (if that segment is needed for the digit)
            segments[i].value(digit_list[i])
            utime.sleep_us(scan_speed)
            segments[i].value(0)

# function to turn off all segments
def display_clear():
    for i in range(8):
        segments[i].value(0)
            

try: 
    while True:
        # set scanning speed in microseconds with potentiometer
        # pot can theoretically read 0 to 65535
        pot_value = pot.read_u16()
        speed_us = int(scale(pot_value, 200, 65000, 0, 10000))
        # turn on the segments for digit 8
        display_char(8, display_time = 500, scan_speed = speed_us)
        print(speed_us)
        
except KeyboardInterrupt:
    # turn off all segments
    display_clear()

            

 



