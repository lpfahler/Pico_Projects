# Mock Display for Shut the Box
# Lori Pfahler
# October 2024

# import modules
from utime import sleep
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
from pimoroni import RGBLED, Button

# setup display
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)
display.set_backlight(1)

# set the font and make some color pens
display.set_font("bitmap8")
BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
PINK = display.create_pen(255, 0, 130)
YELLOW = display.create_pen(255, 255, 0)


# function to clear screen from Pimoroni
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()

# function to make a rectangle outline (rather than a filled rectangle)
def rect_outline(x, y, w, h, thickness = 1):
    display.line(x, y, (x + w - 1), y, thickness)
    display.line((x + w - 1), y, (x + w - 1), (y + h - 1), thickness)
    display.line(x, y, x, (y + h - 1), thickness)
    display.line(x, (y + h - 1), (x + w - 1), (y + h - 1), thickness)

# function to create the numbered tiles to make it easier to make fine adjustments.
# this function has very limited flexibility.  It does NOT center the character or
# make sure it fits inside the outline.  This functionality could be added at a later time.
# The shift of 4 and 5 pixels in the x and y directions to place the character
# works for this application and could be adapted as needed.
def tile(myChar, x, y, w, h, thickness = 1, scale = 4, outCol = (255, 0, 255), charCol = (255, 0, 130)):
    # create pens for the outline color and character color
    outPen = display.create_pen(outCol[0], outCol[1], outCol[2])
    charPen = display.create_pen(charCol[0], charCol[1], charCol[2])
    # draw the outline
    display.set_pen(outPen)
    display.line(x, y, (x + w - 1), y, thickness)
    display.line((x + w - 1), y, (x + w - 1), (y + h - 1), thickness)
    display.line(x, y, x, (y + h - 1), thickness)
    display.line(x, (y + h - 1), (x + w - 1), (y + h - 1), thickness)
    # add the character - shift placement by 4 and 5 pixels in x and y directions
    display.set_pen(charPen)
    display.text(str(myChar), x + 4, y + 5, scale = scale)

# game title 
display.set_pen(WHITE)
display.text('Shut The Box', 70, 0, scale = 3)

# up arrow next to A button
display.set_pen(YELLOW)
display.text('/\\', 0, 47, scale = 2)
# down arrow next to B button
display.set_pen(YELLOW)
display.text('\\/', 0, 167, scale = 2)

# for Y button will need to only show the
# label for the function currently being used
# either to select tiles or to roll the dice (2) 
# "select or roll" next to button Y
display.set_pen(YELLOW)
# one or the other of these two labels
display.text('select ->', 230, 172, scale = 2)
# display.text('roll (2) ->', 225, 175, scale = 2)

# roll one die next to button X
display.set_pen(YELLOW)
display.text('roll (1) ->', 225, 50, scale = 2)

# show roll total and current total of tiles selected
display.text('Roll = ' + str(12), 225, 220, scale = 2)
display.text('Selected = ' + str(12), 0, 220, scale = 2)


# start of a function to draw the dice
def dice(value, x, y): 
    # dice outline
    display.set_pen(WHITE)
    rect_outline(x, y, 52, 52, 1)
    if value == 1:
        display.circle(x + 25, y + 25, 5)
    if value == 2:
        display.circle(x + 12, y + 38, 5) # should be y + 40?
        display.circle(x + 40, y + 12, 5) # or x + 40?
    if value == 3:
        display.circle(x + 12, y + 38, 5) # should be y + 40?
        display.circle(x + 26, y + 25, 5)
        display.circle(x + 40, y + 12, 5) 
    if value == 4:
        display.circle(x + 12, y + 38, 5)
        display.circle(x + 40, y + 12, 5)
        display.circle(x + 12, y + 12, 5)
        display.circle(x + 40, y + 38, 5)
    if value == 5:
        display.circle(x + 12, y + 38, 5)
        display.circle(x + 40, y + 12, 5)
        display.circle(x + 12, y + 12, 5)
        display.circle(x + 40, y + 38, 5)
        display.circle(x + 25, y + 25, 5)
    if value == 6:
        display.circle(x + 12, y + 38, 5)
        display.circle(x + 40, y + 12, 5)
        display.circle(x + 12, y + 12, 5)
        display.circle(x + 40, y + 38, 5)
        display.circle(x + 12, y + 25, 5)
        display.circle(x + 40, y + 25, 5)     

# number tiles
tile('1', 30, 85, 25, 40)
tile('2', 60, 85, 25, 40)
tile('3', 90, 85, 25, 40)
tile('4', 120, 85, 25, 40)
tile('5', 150, 85, 25, 40)
tile('6', 180, 85, 25, 40)
tile('7', 210, 85, 25, 40)
tile('8', 240, 85, 25, 40)
tile('9', 270, 85, 25, 40)


# 6 Die 1
dice(6, 80, 150)
# 6 Die 2
dice(6, 150, 150)

display.update()

