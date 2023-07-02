# Pimon Game with four skill levels (and demo mode)
# Lori Pfahler
# June 2023

# import modules
from machine import Pin, I2C, PWM
from utime import sleep, sleep_ms, ticks_ms, ticks_diff
from random import randint

# setup passive buzzer pim
buzzer = PWM(Pin(16))

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
    if ticks_diff(ticks_ms(), red_debounce_time) > 300:
        red_flag = 1
        red_debounce_time = ticks_ms()

# interrupt function for green button
def green_handler(greenButton):
    global green_debounce_time, green_flag
    if ticks_diff(ticks_ms(), green_debounce_time) > 300:
        green_flag = 1
        green_debounce_time = ticks_ms()

# interrupt function for blue button
def blue_handler(blueButton):
    global blue_debounce_time, blue_flag
    if ticks_diff(ticks_ms(), blue_debounce_time) > 300:
        blue_flag = 1
        blue_debounce_time = ticks_ms()

# interrupt function for yellow button
def yellow_handler(yellowButton):
    global yellow_debounce_time, yellow_flag
    if ticks_diff(ticks_ms(), yellow_debounce_time) > 300:
        yellow_flag = 1
        yellow_debounce_time = ticks_ms()

# interrupt requests
redButton.irq(trigger = Pin.IRQ_RISING, handler = red_handler)
greenButton.irq(trigger = Pin.IRQ_RISING, handler = green_handler)
blueButton.irq(trigger = Pin.IRQ_RISING, handler = blue_handler)
yellowButton.irq(trigger = Pin.IRQ_RISING, handler = yellow_handler)

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

# function to compare list (game vs player) and make losing sound if not a match
def list_match(list1, list2):
    if list1 == list2:
        end_game = False
    else:
        tone(buzzer, 100, 2000)
        end_game = True
    return(end_game)        

# initialize tone_number
tone_number = 1

# set the sequence length
print('Welcome to Pimon!\n')
print('Enter the Number for Skill Level You Want to Play')
print('Beginner: match 8 colors, Intermediate: 14, Advanced: 20, Expert: 31, Demo: 4\n')
correct_input = False
while correct_input == False:
    choice = input('8 = Beginner, 14 = Intermediate, 20 = Advanced, 31 = Expert, 4 = Demo:  ')
    if choice in ['4', '8', '14', '20', '21']:
        n_seq = int(choice)
        correct_input = True
        print(f'Match the {n_seq} colors to win!')
        sleep(2)
    else:
        print('Not a valid choice - please try again')


# create a random sequence of the numbers 1-4
game_seq = []
for i in range(0, n_seq):
    game_seq.append(randint(1, 4))


try:
    while tone_number <= n_seq:
        # play the game sequence up to the current value of tone_number
        play_seq(buzzer, game_seq, tone_number, 500)
        # get sequence input from the player
        player_seq = []
        while len(player_seq) < tone_number:
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
        # compare player's sequence to game sequence        
        game_over = list_match(game_seq[0:tone_number], player_seq)
        # determine if player has lost or won or game should continue
        if game_over == True:
            tone_number = n_seq + 1   # makes game end
            print('Game Over - You Lose')
        elif game_over == False and tone_number == n_seq:
            tone_number = n_seq + 1   # makes game end
            print('YOU WIN!')
        else:
            tone_number += 1
        sleep(1)
        
        
except KeyboardInterrupt:
    redLED.value(0)
    greenLED.value(0)
    blueLED.value(0)
    yellowLED.value(0)
