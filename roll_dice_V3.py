# Roll the Dice for Shut the Box Game
# Lori Pfahler
# October 2024

# import modules
from utime import sleep
from random import randint
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
from pimoroni import RGBLED, Button
import stb

# create display
myDisplay = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)
myDisplay.set_backlight(1)

# set the font and make some color pens
myDisplay.set_font("bitmap8")
BLACK = myDisplay.create_pen(0, 0, 0)
WHITE = myDisplay.create_pen(255, 255, 255)
MAGENTA = myDisplay.create_pen(255, 0, 255)
PINK = myDisplay.create_pen(255, 0, 130)
YELLOW = myDisplay.create_pen(255, 255, 0)

# Initialize built-in RGB LED and two button switches
myLED = RGBLED(6, 7, 8)
button_x = Button(14)
button_y = Button(15) 

# labels for buttons X (roll 1) and Y (roll 2)
myDisplay.set_pen(YELLOW)
myDisplay.text('roll (2) ->', 225, 175, scale = 2)
myDisplay.text('roll (1) ->', 225, 50, scale = 2)
myDisplay.update()

# turn on built-in RGB LED off
myLED.set_rgb(0, 0, 0)

while True:
    if button_x.read():
        stb.rollOne(myDisplay, myLED)
        # clear second die
        myDisplay.set_pen(BLACK)
        myDisplay.rectangle(150, 150, 52, 52)
        myDisplay.update()
    if button_y.read():
        stb.rollTwo(myDisplay, myLED)  
    sleep(0.1)

