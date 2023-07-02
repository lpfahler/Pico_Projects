# Pimon - building block program 3
# Code for player to enter their color/sound sequence
# Lori Pfahler
# June 2023

# import modules
from machine import Pin, I2C, PWM
from utime import sleep, sleep_ms, ticks_ms, ticks_diff
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
    
# dictionary for the game buttons: 1 = red, 2 = green, 3 = blue, 4 = yellow 
button_dict = {
    1 : (311, [1, 0, 0, 0]),
    2 : (415, [0, 1, 0, 0]),
    3 : (208, [0, 0, 1, 0]),
    4 : (247,  [0, 0, 0, 1])
    }

# setup the four LEDs
redLED = Pin(14, Pin.OUT)
greenLED = Pin(12, Pin.OUT)
blueLED = Pin(10, Pin.OUT)
yellowLED = Pin(8, Pin.OUT)

# setup buttons
redButton = Pin(15, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(13, Pin.IN, Pin.PULL_DOWN)
blueButton = Pin(11, Pin.IN, Pin.PULL_DOWN)
yellowButton = Pin(9, Pin.IN, Pin.PULL_DOWN)

# variables to track interrupt activation and time for debouncing
red_debounce_time = ticks_ms()
green_debounce_time = ticks_ms()
blue_debounce_time = ticks_ms()
yellow_debounce_time = ticks_ms()
red_flag = 0
green_flag = 0
blue_flag = 0
yellow_flag = 0

# interrupt function for red button
def red_handler(redButton):
    global red_debounce_time, red_flag
    if ticks_diff(ticks_ms(), red_debounce_time) > 400:
        red_flag = 1
        red_debounce_time = ticks_ms()

# interrupt function for green button
def green_handler(greenButton):
    global green_debounce_time, green_flag
    if ticks_diff(ticks_ms(), green_debounce_time) > 400:
        green_flag = 1
        green_debounce_time = ticks_ms()

# interrupt function for blue button
def blue_handler(blueButton):
    global blue_debounce_time, blue_flag
    if ticks_diff(ticks_ms(), blue_debounce_time) > 400:
        blue_flag = 1
        blue_debounce_time = ticks_ms()

# interrupt function for yellow button
def yellow_handler(yellowButton):
    global yellow_debounce_time, yellow_flag
    if ticks_diff(ticks_ms(), yellow_debounce_time) > 400:
        yellow_flag = 1
        yellow_debounce_time = ticks_ms()

# interrupt requests
redButton.irq(trigger = Pin.IRQ_RISING, handler = red_handler)
greenButton.irq(trigger = Pin.IRQ_RISING, handler = green_handler)
blueButton.irq(trigger = Pin.IRQ_RISING, handler = blue_handler)
yellowButton.irq(trigger = Pin.IRQ_RISING, handler = yellow_handler)


# initialize player_seq and set the seq_length
player_seq = []
n_seq = 8
print(f'Enter {n_seq} button presses')


try:
    while len(player_seq) < n_seq:
        if red_flag == 1:
            red_flag = 0
            player_seq.append(1)
            redLED.value(1)
            tone(buzzer, button_dict[1][0], 250)
            redLED.value(0)
        if green_flag == 1:
            green_flag = 0
            player_seq.append(2)
            greenLED.value(1)
            tone(buzzer, button_dict[2][0], 250)
            greenLED.value(0)
        if blue_flag == 1:
            blue_flag = 0
            player_seq.append(3)
            blueLED.value(1)
            tone(buzzer, button_dict[3][0], 250)
            blueLED.value(0)
        if yellow_flag == 1:
            yellow_flag = 0
            player_seq.append(4)
            yellowLED.value(1)
            tone(buzzer, button_dict[4][0], 250)
            yellowLED.value(0)       

    print(player_seq)

except KeyboardInterrupt:
    redLED.value(0)
    greenLED.value(0)
    blueLED.value(0)
    yellowLED.value(0)