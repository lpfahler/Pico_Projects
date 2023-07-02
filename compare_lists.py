# Pimon - building block program 4
# Code for comparing device sequence to player entered sequence
# Lori Pfahler
# June 2023

# import modules
from machine import Pin, I2C, PWM
from utime import sleep, sleep_ms
from random import randint

# setup passive buzzer pim
buzzer = PWM(Pin(16))

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

# compare lists for exact match
device1 = [1, 2, 3, 4, 1, 2, 3, 4]
player1 = [1, 2, 3, 4, 1, 2, 3, 4]
player2 = [1, 2, 3, 4, 1, 2, 3, 3]

# function to compare and make losing sound if not a match
def list_match(list1, list2):
    if list1 == list2:
        print('match')
        end_game = False
    else:
        print('not a match')
        tone(buzzer, 100, 500)
        end_game = True
    return(end_game)  


game_over = list_match(device1, player1)
print('Is the game over?',game_over)

sleep(2)

game_over = list_match(device1, player2)
print('Is the game over?', game_over)