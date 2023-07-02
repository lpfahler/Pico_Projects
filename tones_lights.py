# Pimon - building block program 2
# Code for lighting a sequence and also playing tone along with it
# Lori Pfahler
# June 2023

# import modules
from machine import Pin, I2C, PWM
from utime import sleep, sleep_ms
from random import randint

# setup passive buzzer pim
buzzer = PWM(Pin(16))

# setup the four LEDs
redLED = Pin(14, Pin.OUT)
greenLED = Pin(12, Pin.OUT)
blueLED = Pin(10, Pin.OUT)
yellowLED = Pin(8, Pin.OUT)

# function to play a note/tone on a passive buzzer using PWM
def tone(pin, frequency, duration):
    # set the pin frequency
    pin.freq(frequency)
    # use a duty cycle of 50% - can be set from 0 to 65535
    pin.duty_u16(32768)
    # hold the note for the duration needed
    sleep_ms(duration)
    # turn the sound off
    pin.duty_u16(0)
    # a little bit of sleep to create a "break' between notes
    sleep_ms(50)
    
# function to play sequence of red, green, blue and yellow LEDs with
# appropriate sounds, n = how much of the sequence to play
def play_seq(pin, seq, n, duration):
    for i in seq[0:n]:
        # print(i)
        # get the needed freq for button i from button_dict
        freq = button_dict[i][0]
        # light the LEDs for button i from button_dict
        redLED.value(button_dict[i][1][0])
        greenLED.value(button_dict[i][1][1])
        blueLED.value(button_dict[i][1][2])
        yellowLED.value(button_dict[i][1][3])
        # play the tone for button i
        tone(pin, freq, duration)
        # briefly turn off the LEDs to create blink if the same button comes next
        redLED.value(0)
        greenLED.value(0)
        blueLED.value(0)
        yellowLED.value(0)
        sleep_ms(50)
        
# dictionary for the game buttons: 1 = red, 2 = green, 3 = blue, 4 = yellow 
button_dict = {
    1 : (311, [1, 0, 0, 0]),
    2 : (415, [0, 1, 0, 0]),
    3 : (208, [0, 0, 1, 0]),
    4 : (247,  [0, 0, 0, 1])
    }

# create a random sequence of the numbers 1-4
game_seq = []
# set the sequence length
n_seq = 8
for i in range(0, n_seq):
    game_seq.append(randint(1, 4))
    
print(game_seq)

# play sound and light the LEDs for the sequence
play_seq(buzzer, game_seq, 8, 500)

# play a sequence in steps - needed for game play
for i in range(0, len(game_seq)+1):
    play_seq(buzzer, game_seq, i, 500)
    sleep(2)

