# Select Tiles for Shut the Box Game
# Does not allow unselecting a tile
# Lori Pfahler
# October 2024

# import modules
from utime import sleep
from random import randint
# If you have a Pico Display (smaller display) use DISPLAY_PICO_DISPLAY
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
from pimoroni import RGBLED, Button
import stb

# If you have a Pico Display (smaller display) use DISPLAY_PICO_DISPLAY
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
led = RGBLED(6, 7, 8)
button_a = Button(12)
button_b = Button(13)
button_y = Button(15)
    
# up arrow next to A button
myDisplay.set_pen(YELLOW)
myDisplay.text('/\\', 0, 47, scale = 2)
# down arrow next to B button
myDisplay.text('\\/', 0, 167, scale = 2)
# select next to Y button
myDisplay.text('select ->', 230, 172, scale = 2)
# display tiles
stb.tiles(myDisplay, active = [1, 2, 3, 4, 5, 6, 7, 8, 9])
myDisplay.update()
# turn on built-in RGB LED off
led.set_rgb(0, 0, 0)


# loop control - set rollTotal to seven to test program
selTotal = 0
rollTotal = 7

currentTile = 0
tileNum = 1
myDisplay.set_pen(YELLOW)
myDisplay.rectangle(30, 130, 25, 5)
myDisplay.text('Roll = ' + str(rollTotal), 225, 220, scale = 2)
myDisplay.text('Selected = ' + str(selTotal), 0, 220, scale = 2)
myDisplay.update()


availTiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]


while selTotal != rollTotal:
    print(currentTile)
    
    if button_a.read():
        # remove previous marker
        myDisplay.set_pen(BLACK)        
        myDisplay.rectangle((30 + (30 * currentTile)), 130, 25, 5)
        # increase marker one tile
        currentTile = (currentTile + 1) % 9
    

    if button_b.read():
        # remove previous marker
        myDisplay.set_pen(BLACK)
        myDisplay.rectangle((30 + (30 * currentTile)), 130, 25, 5)
        # decrease marker one tile
        currentTile = (currentTile - 1) % 9

    # put marker under current tile 
    myDisplay.set_pen(YELLOW)
    myDisplay.rectangle((30 + (30 * currentTile)), 130, 25, 5)
    myDisplay.update()
    sleep(0.1)
    
    if button_y.read():
        # grey out number to indicate selected
        # stb.tile(myDisplay, str(currentTile + 1), (30 + (30 * currentTile)), 85, 25, 40, charCol = (128, 128, 128))
        availTiles.remove(currentTile + 1)
        stb.tiles(myDisplay, active = availTiles)        
        # add number to selected tile list
        selTotal = selTotal + currentTile + 1
        myDisplay.set_pen(BLACK)
        myDisplay.rectangle(0, 220, 180, 20)
        myDisplay.set_pen(YELLOW)
        myDisplay.text('Selected = ' + str(selTotal), 0, 220, scale = 2)
        myDisplay.update()
        
    
    
    
    
    
    