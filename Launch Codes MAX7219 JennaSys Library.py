# Using 8-Digit 7-Segment Display with MAX7219 Driver Chip
#
# Using JennaSys's library: https://github.com/JennaSys/micropython-max7219
# VCC to 3.3V rail
# GND Pin to GND rail
# DIN Pin to SPI0 TX - GP19
# CS Pin to SPI0 CSn - GP17
# CLK Pin to SPI0 SCK - GP18
#
# W.O.P.R Missle Launch Sequence
# Unfortunately the JennaSys library does not seem to handle the second display correctly
# We see brief flashes of duplicate digits on the second display
#
# Lori Pfahler
# August 2025

from machine import Pin, SPI
import utime
import max7219
import random

# set up the SPI bus
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19))
cs = Pin(17, Pin.OUT)

# set up the display
display = max7219.SevenSegment(digits=16, scan_digits=8, cs=cs, spi_bus=0, reverse=True)

# list of alphabet and digits to randomly select from
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# provide the final launch code 
final_code = ['C', 'P', 'E', '1', '7', '0', '4', 'T', 'K', 'S']
# list to hold the current code
cur_code = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# loop over the positions needed to build the full code 
# 6 with letters, 4 with digits
for i in range(10):
    # find the final code in a random number of loops
    num_loops = random.randint(10, 30)
    for j in range(5, num_loops):
        # loop over the positions in the code and randomly select a letter or number as needed
        for k in range(10):
            if k in [0, 1, 2, 7, 8, 9]:
                cur_code[k] = random.choice(letters)
                # make sure current random choice is not the final_code for the position k
                while cur_code[k] == final_code[k]:
                    cur_code[k] = random.choice(letters)
            if k in [3, 4, 5, 6]:
                cur_code[k] = random.choice(digits)
                # make sure current random choice is not the final_code for the position k                
                while cur_code[k] == final_code[k]:
                    cur_code[k] = random.choice(digits)
        # show this code on display
        print_code = final_code[0:i] + cur_code[i:10]
        # on the last set of loops make the print_code equal to the final_code
        if i == 9 and j == (num_loops - 1):
            print_code = final_code
        # insert the blanks into print_code
        print_code.insert(3, ' ')
        print_code.insert(8, ' ')
        # print for debugging and to see operation of the loops
        # print(f'i = {i}, j = {j}, num_loops = {num_loops}, code = {print_code}')
        # make print_code a string for printing
        display.text(''.join(print_code))
        # short delay
        utime.sleep(0.1)


utime.sleep(30)

# clear the display
display.clear()
    
        
