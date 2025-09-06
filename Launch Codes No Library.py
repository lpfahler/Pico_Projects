# Using 8-Digit 7-Segment Display with MAX7219 Driver Chip
#
# No Library! Two Displays
# W.O.P.R Missle Launch Sequence - Program 4
#
# VCC to 5V rail
# GND Pin to GND rail
# DIN Pin to SPI0 TX - GP19
# CS Pin to SPI0 CSn - GP17
# CLK Pin to SPI0 SCK - GP18
#
# Lori Pfahler
# August 2025

from machine import Pin, SPI
import utime
import random

# Control pins for display
DIN = Pin(19, Pin.OUT)
CLK = Pin(18, Pin.OUT)
CS = Pin(17, Pin.OUT) # also called LOAD on some display modules

# set up the SPI bus
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=CLK, mosi=DIN)

# define register addresses
NOOP = 0x00
DIGIT0 = 0x01 # right-most digit
DIGIT1 = 0x02
DIGIT2 = 0x03
DIGIT3 = 0x04
DIGIT4 = 0x05
DIGIT5 = 0x06
DIGIT6 = 0x07
DIGIT7 = 0x08 # left-most digit
DECODEMODE = 0x09
INTENSITY = 0x0A
SCANLIMIT = 0x0B
SHUTDOWN = 0x0C
DISPLAYTEST = 0x0F

# character map in binary format for readability/modification ease
# segment order is DP, A, B, C, D, E, F, G - order needed for MAX7219
# adapted from https://github.com/pdwerryhouse/max7219_8digit
CHAR_MAP = {
    '0': 0b01111110, '1': 0b00110000, '2': 0b01101101, '3': 0b01111001,
    '4': 0b00110011, '5': 0b01011011, '6': 0b01011111, '7': 0b01110000,
    '8': 0b01111111, '9': 0b01111011, 'a': 0b01110111, 'b': 0b00011111,
    'c': 0b01001110, 'd': 0b00111101, 'e': 0b01001111, 'f': 0b01000111,
    'g': 0b01111011, 'h': 0b00110111, 'i': 0b00110000, 'j': 0b00111100,
    'k': 0b01010111, 'l': 0b00001110, 'm': 0b01010100, 'n': 0b00010101,
    'o': 0b00011101, 'p': 0b01100111, 'q': 0b01110011, 'r': 0b00000101,
    's': 0b01011011, 't': 0b00001111, 'u': 0b00011100, 'v': 0b00111110,
    'w': 0b00101010, 'x': 0b00110111, 'y': 0b00111011, 'z': 0b01101101,
    'A': 0b01110111, 'B': 0b00011111, 'C': 0b01001110, 'D': 0b00111101, 
    'E': 0b01001111, 'F': 0b01000111, 'G': 0b01111011, 'H': 0b00110111, 
    'I': 0b00110000, 'J': 0b00111100, 'K': 0b01010111, 'L': 0b00001110, 
    'M': 0b01010100, 'N': 0b00010101, 'O': 0b00011101, 'P': 0b01100111, 
    'Q': 0b01110011, 'R': 0b00000101, 'S': 0b01011011, 'T': 0b00001111, 
    'U': 0b00011100, 'V': 0b00111110, 'W': 0b00101010, 'X': 0b00110111, 
    'Y': 0b00111011, 'Z': 0b01101101, ' ': 0b00000000, '-': 0b01000000, 
    '.': 0b10000000, '*': 0b01100011, "'": 0b00000010, ',': 0b00011000,
    '=': 0b00001001, '!': 0b10000110, '<': 0b01100001, '>': 0b01000011,
    '?': 0b11100101, '@': 0b01111101, '+': 0b00110001,
}

# function to lookup a character in CHAR_MAP
def get_char(char):
    value = CHAR_MAP.get(char)
    if value == None:
        value = 0b00000000
    return value

# variable to use decode mode (True) or no decode mode (False)
# you can change decodemode value(s) per position as needed at start of program
# I think all on or all off would be the most likely choices
decode = False

# send commands and values for two displays
# Must send No-Op command to display that is not being addressed (0x00, 0x00) or (NOOP, 0x00)
def send_cmd(address1, value1, address2, value2):
    CS.value(0)
    spi.write(bytes([address2, value2]))
    spi.write(bytes([address1, value1]))
    CS.value(1)
    
# blank/clear two displays
def clear():
    global decode
    # if decode is True
    if decode == True:
        # clear first display - send blank
        for value in range(1, 9):
            send_cmd(NOOP, 0x00, value, 0x0F)
        # clear second display - send blank
        for value in range(1, 9):
            send_cmd(value, 0x0F, NOOP, 0x00)
    else:
    # if decode is False
        # clear second display - send 0b00000000 (0x00)
        for value in range(1, 9):
            send_cmd(NOOP, 0x00, value, 0b00000000)
        # clear second display - send 0b00000000 (0x00)
        for value in range(1, 9):
            send_cmd(value, 0b00000000, NOOP, 0x00)        

# initialize
def initialize():
    global decode
    # set CS pin to high
    CS.value(1)
    # write test command off
    send_cmd(DISPLAYTEST, 0x00, NOOP, 0x00)
    send_cmd(NOOP, 0x00, DISPLAYTEST, 0x00)
    # set normal operation
    send_cmd(SHUTDOWN, 0x01, NOOP, 0x00)
    send_cmd(NOOP, 0x00, SHUTDOWN, 0x01)
    # enable all digits
    send_cmd(SCANLIMIT, 0x07, NOOP, 0x00)
    send_cmd(NOOP, 0x00, SCANLIMIT, 0x07)
    # set brightness
    send_cmd(INTENSITY, 0x05, NOOP, 0x00)
    send_cmd(NOOP, 0x00, INTENSITY, 0x05)
    # if decode = True, turn on decode mode for all digits
    if decode == True:
        send_cmd(DECODEMODE, 0xFF, NOOP, 0x00)
        send_cmd(NOOP, 0x00, DECODEMODE, 0xFF)
    # if decode = False, turn decode mode off for all digits
    else:
        send_cmd(DECODEMODE, 0x00, NOOP, 0x00)
        send_cmd(NOOP, 0x00, DECODEMODE, 0x00)
    # clear display
    clear()





initialize()


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
    for j in range(num_loops):
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
        # first display characters - reversed 
        code_1_reversed = list(reversed(print_code[0:8]))
        for index, char in enumerate(code_1_reversed):
            send_cmd(index + 1, get_char(char), NOOP, 0x00)
        # second display characters - reversed  
        code_2_reversed = list(reversed(print_code[8:12]))
        for index, char in enumerate(code_2_reversed):
            send_cmd(NOOP, 0x00, index + 5, get_char(char))   
        # short delay
        utime.sleep(0.1)

       
utime.sleep(30)
# clear displays
clear()