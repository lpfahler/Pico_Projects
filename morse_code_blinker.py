# Program to blink Morse Code on an LED based on
# user entered message.
# Inspired by Simon Monk's Programming the Pico
# Lori Pfahler
# Feb 2023

# import libraries
from machine import Pin
from utime import sleep

# setup LED
redLED = Pin(15, Pin.OUT)

# create needed sleep times for 10 words per minute dot = 0.12 seconds
# 5 words per minute is 0.24 seconds
dot = 0.24
dash = 3 * dot
withinChar = dot
betChar = 3 * dot
betWord = 7 * dot

# make sure LED is off
redLED.off()

# dictionary for letters and numbers linked to the Morse code for that character
morseCode = {
    'a' : '.-',    'b' : '-...',  'c' : '-.-.',
    'd' : '-..',   'e' : '.',     'f' : '..-.',
    'g' : '--.',   'h' : '....',  'i' : '..',
    'j' : '.---',  'k' : '-.-',   'l' : '.-..',
    'm' : '--',    'n' : '-.',    'o' : '---',
    'p' : '.--.',  'q' : '--.-',  'r' : '.-.',
    's' : '...',   't' : '-',     'u' : '..-',
    'v' : '...-',  'w' : '.--',   'x' : '-..-',
    'y' : '-.--',  'z' : '--..',  '1' : '.----',
    '2' : '..---', '3' : '...--', '4' : '....-',
    '5' : '.....', '6' : '-....', '7' : '--...',
    '8' : '---..', '9' : '----.', '0' : '-----'
    }

# function for blinking the LED for a particular letter or number
def charBlinks(char):
    # if the character is a space, sleep the between word time
    if char == ' ':
        # assuming that the space is inside the message (not the first character)
        # for a space, we need to sleep "betWord - 3" since the blinking code always sleeps
        # betChar (=3) at the end of each character
        sleep(betWord - 3)
    else:
        # look up character in morseCode dictionary - make lowercase if needed
        mCode = morseCode.get(char.lower())
        # if the code is found - blink the code
        if mCode:
            print(char, mCode)
            # need to know number of dot/dashes to do the between character timing
            lenCode = len(mCode)
            # counter to know when we get to the last dot/dash in mCode
            count = 0
            for symbol in mCode:
                # tract place in mCode
                count += 1
                if symbol == '.':
                    # blink a dot
                    redLED.on()
                    sleep(dot)
                    redLED.off()
                    if count == lenCode:
                        # character blinks finished - sleep the between character time
                        sleep(betChar)
                    else:
                        sleep(withinChar)
                if symbol == '-':
                    # blink a dash
                    redLED.on()
                    sleep(dash)
                    redLED.off()
                    if count == lenCode:
                        # character blinks finished - sleep the between character time
                        sleep(betChar)
                    else:
                        sleep(withinChar)
        else:
            # print this if the code for the character is not found
            print('No Morse code for this character:', char)
    
while True:
    myMessage = input('Enter Your Message (a-z, 0-9): ')
    for char in myMessage:
        charBlinks(char)

    

