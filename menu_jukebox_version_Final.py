# Buzzer Jukebox for Pico W with OLED Display for Menu System
# Two Color OLED SSD1315 - Menu will display in (0,16)-(127,63) blue pixel area
# Lori Pfahler
# April 2023
#
# Includes parts of Kevin McAleer's code to create the menu
# Kevin's original code @
# https://github.com/kevinmcaleer/rotarydisplay/blob/main/rotary_display.py

# import modules
from machine import Pin, I2C, PWM
import utime
import sys
from ssd1306 import SSD1306_I2C
import framebuf
import songs
import song_player

# setup I2C bus and display
i2c=I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
myOLED = SSD1306_I2C(128, 64, i2c, addr = 0x3c)
myOLED.init_display()

# setup passive buzzer pim
buzzer = PWM(Pin(7))

# setup buttons
downButton = Pin(15, Pin.IN, Pin.PULL_DOWN)
upButton = Pin(14, Pin.IN, Pin.PULL_DOWN)
selectButton = Pin(13, Pin.IN, Pin.PULL_DOWN)

# variables to track interrupt activation and time for debouncing
debounce_time = 0
down_flag = 0
up_flag = 0
select_flag = 0

# interrupt function for down button
def down_handler(downButton):
    global menuPosition, debounce_time, down_flag
    if (utime.ticks_ms()-debounce_time) > 300:
        down_flag = 1
        debounce_time=utime.ticks_ms()

# interrupt function for up button
def up_handler(upButton):
    global menuPosition, debounce_time, up_flag
    if (utime.ticks_ms()-debounce_time) > 300:
        up_flag = 1
        debounce_time=utime.ticks_ms()

# interrupt function for select button
def select_handler(selectButton):
    global menuPosition, debounce_time, select_flag
    if (utime.ticks_ms()-debounce_time) > 300:
        select_flag = 1
        debounce_time=utime.ticks_ms()

# interrupt requests
downButton.irq(trigger=Pin.IRQ_RISING, handler=down_handler)
upButton.irq(trigger=Pin.IRQ_RISING, handler=up_handler)
selectButton.irq(trigger=Pin.IRQ_RISING, handler=select_handler)

# Menu Screen Variables
# only using the bottom (blue portion of the OLED)
# blue portion has height of 48 pixel lines - covers pixels(0,16)-(127,63)
width = 128
height = 48
line = 1 
highlight = 1
shift = 0
list_length = 0
total_lines = 4

menuList = ['StarWars', 'Take Me On', 'Game of Thrones', 'StarTrek',
            'Harry Potter', 'Margaritaville', 'Ode To Joy', 'Quit']

# function to create the menu of the OLED display
def show_menu(menu):
    # bring in the global variables
    global line, highlight, shift, list_length
    # menu variables
    item = 1
    line = 1
    # use 12 pixels for each line - place text (8x8 pixels format) inside with
    # two pixel border on top and botton
    line_height = 12
    # clear the display
    myOLED.fill_rect(0, 16, width, height, 0)
    # Shift the list of files so that it shows on the display
    list_length = len(menu)
    short_list = menu[shift:shift+total_lines]
    for item in short_list:
        if highlight == line:
            myOLED.fill_rect(0, ((line-1)*line_height + 16), width, line_height, 1)
            # place text with two pixels below filled rectangle
            myOLED.text(">",0, ((line-1)*line_height + 18), 0)
            myOLED.text(item, 10, ((line-1)*line_height + 18), 0)
            myOLED.show()
        else:
            myOLED.text(item, 10, ((line-1)*line_height + 18), 1)
            myOLED.show()
        line += 1 

# show title in the yellow area of the OLED (0,0) - (127, 15)
myOLED.text('Buzzer Jukebox', 10, 4, 1)
myOLED.hline(0, 0, width, 1)
myOLED.hline(0, 14, width, 1)
# show menu for the first time
myOLED.show()
show_menu(menuList)
print('Start')
print('HL=',highlight, 'shift =', shift)

while True:
    # down button pressed
    if down_flag == 1:
        down_flag = 0
        if highlight < total_lines:
            highlight += 1
        else: 
            if shift+total_lines < list_length:
                shift += 1
        show_menu(menuList)
        print('Down button pressed')
        print('hightlight =',highlight, 'shift =', shift)
    # up button pressed
    if up_flag == 1:
        up_flag = 0
        if highlight > 1:
            highlight -= 1  
        else:
            if shift > 0:
                shift -= 1
        show_menu(menuList)
        print('Up button pressed')
        print('highlight =',highlight, 'shift =', shift)
    # select button pressed
    if select_flag == 1:
        select_flag = 0
        # determine which song to play in menuList
        menuPosition = (highlight - 1) + shift
        if menuPosition == 0:
            song_player.playsong(buzzer, songs.starWars, tempo = 1500) 
        if menuPosition == 1:     
            song_player.playsong(buzzer, songs.takeMeOn, tempo = 2000)
        if menuPosition == 2:
            song_player.playsong(buzzer, songs.gameOfThrones, tempo = 2000)
        if menuPosition == 3:
            song_player.playsong(buzzer, songs.starTrekIntro, tempo = 3000)
        if menuPosition == 4:
            song_player.playsong(buzzer, songs.harryPotter, tempo = 1000)
        if menuPosition == 5:
            song_player.playsong(buzzer, songs.margaritaville, tempo = 1500)
        if menuPosition == 6:
            song_player.playsong(buzzer, songs.odeToJoy, tempo = 1500)
        if menuPosition == 7:
            # clear screen and quit program
            myOLED.fill(0)
            myOLED.show()
            sys.exit()
 
        
