# Shut the Box Game Code for PicoDisplay 2.0
# Lori Pfahler
# July 2024

# imports 
from utime import sleep
from random import randint
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
from pimoroni import RGBLED, Button
import random
import stb

# create display object
myDisplay = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)
myDisplay.set_backlight(1)

# set the font and make some color pens
myDisplay.set_font("bitmap8")
BLACK = myDisplay.create_pen(0, 0, 0)
WHITE = myDisplay.create_pen(255, 255, 255)
MAGENTA = myDisplay.create_pen(255, 0, 255)
PINK = myDisplay.create_pen(255, 0, 130)
YELLOW = myDisplay.create_pen(255, 255, 0)

# Initialize built-in RGB LED and four button switches
myLED = RGBLED(6, 7, 8)
button_a = Button(12) # up tile list
button_b = Button(13) # down tile list
button_x = Button(14) # roll 1
button_y = Button(15) # select or roll 2

# turn on built-in RGB LED off
myLED.set_rgb(0, 0, 0)


while True:
    # control variable
    gameOver = False
    availTiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    currTile = 1
    rollDice = False
    # game display initial setup:
    stb.start(myDisplay)
    sleep(5)

    # loop for game play
    while gameOver == False:
        
        # blank out dice
        stb.dice(myDisplay, 0, 80, 150)
        stb.dice(myDisplay, 0, 150, 150)
        
        # check for Score = 0 - User Wins
        if sum(availTiles) == 0:
            gameOver == True
            stb.clear(myDisplay)
            myDisplay.update()
            stb.message(myDisplay, text = 'Score = 0, You Win!', x = 0, y = 0, scale = 3)
            sleep(3)
            continue
            
        # check to see if one die can be used
        if max(availTiles) <= 6:
            stb.message(myDisplay, text = 'Roll 1 or 2', x = 0, y = 0, scale = 3)
            stb.labelY(myDisplay, text = 'roll (2) ->')
            stb.labelX(myDisplay, text = 'roll (1) ->')
            while rollDice == False:
                if button_x.read():
                    # clear second die
                    myDisplay.set_pen(BLACK)
                    myDisplay.rectangle(150, 150, 52, 52)
                    myDisplay.update()
                    rollTotal = stb.rollOne(myDisplay, myLED)
                    rollDice = True
                if button_y.read():
                    rollTotal = stb.rollTwo(myDisplay, myLED)
                    rollDice = True
        else:
            stb.message(myDisplay, text = 'Roll 2', x = 0, y = 0, scale = 3)
            stb.labelY(myDisplay, text = 'roll (2) ->')
            stb.labelX(myDisplay, text = ' ')
            while rollDice == False:
                if button_y.read():
                    rollTotal = stb.rollTwo(myDisplay, myLED)
                    rollDice = True
        sleep(0.1)

        # check to see if this roll has any possible solutions in availTiles
        if stb.rollCheck(rollTotal, availTiles) == False:
            stb.message(myDisplay, text = 'No play available', x = 0, y = 0, scale = 3)
            sleep(3)
            stb.clear(myDisplay)
            myDisplay.update()
            stb.message(myDisplay, text = 'Score = ' + str(sum(availTiles)), x = 0, y = 0, scale = 3)
            sleep(5)
            # skip selection loop and end game
            selDone = True
            gameOver = True
        else:
            # solutions exist for roll - begin tile selection
            currentTile = 0
            # place cursor under tile 1
            myDisplay.set_pen(YELLOW)
            myDisplay.rectangle(30, 130, 25, 5)
            # select tiles
            stb.message(myDisplay, text = 'Select tiles', x = 0, y = 0, scale = 3)
            stb.labelY(myDisplay, text = ' Select ->')
            stb.labelX(myDisplay, text = ' ')
            # variables to manage user tile selection
            selDone = False
            curChoices = []
            
        while selDone == False:
            # move cursor with buttons A and B   
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
                # select numbers
                curSelection = currentTile + 1
                if curSelection in curChoices:
                    # if user selects a tile that they have already 
                    # selected for this roll, return tile to normal colors
                    # return selection to availTiles list
                    curChoices.remove(curSelection)
                    availTiles.append(curSelection)
                    stb.tiles(myDisplay, active = availTiles)
                    myDisplay.set_pen(BLACK)
                    myDisplay.rectangle(0, 220, 180, 20)
                    myDisplay.set_pen(YELLOW)
                    myDisplay.text('Selected = ' + str(sum(curChoices)), 0, 220, scale = 2)
                    myDisplay.update() 
                elif curSelection not in availTiles:
                    # if selection is not available, go to top of while loop
                    stb.message(myDisplay, text = 'Tile Not Available', x = 0, y = 0, scale = 3)
                    continue                   
                else:
                    # append choice to curChoices array - grey out tile
                    # remove from availTiles list
                    curChoices.append(curSelection)
                    availTiles.remove(curSelection)
                    stb.tiles(myDisplay, active = availTiles)
                    myDisplay.set_pen(BLACK)
                    myDisplay.rectangle(0, 220, 180, 20)
                    myDisplay.set_pen(YELLOW)
                    myDisplay.text('Selected = ' + str(sum(curChoices)), 0, 220, scale = 2)
                    myDisplay.update()
                    
            if sum(curChoices) == rollTotal:
                # if sum(curChoices) equals the rollTotal - end selection
                sleep(2)
                selDone = True
                rollDice = False
                # clear selected and roll text at bottom of screen
                myDisplay.set_pen(BLACK)
                myDisplay.rectangle(0, 220, 320, 20)
                # remove previous marker
                myDisplay.set_pen(BLACK)        
                myDisplay.rectangle((30 + (30 * currentTile)), 130, 25, 5)
                myDisplay.update()


