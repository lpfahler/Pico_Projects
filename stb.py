# Functions for Shut the Box Game
# Lori Pfahler
# October 2024

from utime import sleep
from random import randint

# function to clear screen from Pimoroni
def clear(display):
    BLACK = display.create_pen(0, 0, 0)
    display.set_pen(BLACK)
    display.clear()
    display.update()

# function for initial screen setup
def start(display):
    # clear display
    clear(display)
    display.set_font("bitmap8")
    # game title 
    message(display, text = 'Shut The Box', x = 70, y = 0, scale = 3)
    # Starting labels
    YELLOW = display.create_pen(255, 255, 0)
    display.set_pen(YELLOW)
    # next to Y button
    # labelY(display, text = 'roll (2) ->')
    # next to X button
    # labelX(display, text = 'roll (1) ->')
    # down arrow next to B button
    display.text('/\\', 0, 47, scale = 2)
    # down arrow next to B button
    display.text('\\/', 0, 167, scale = 2)
    # display tiles
    tiles(display, active = [1, 2, 3, 4, 5, 6, 7, 8, 9])
    # place dice on display
    dice(display, 6, 80, 150)
    dice(display, 6, 150, 150)
    display.update()
    
    
def labelY(display, text = "Roll(2) ->"):    
        # clear previous label for Y button
        BLACK = display.create_pen(0, 0, 0)
        YELLOW = display.create_pen(255, 255, 0)
        display.set_pen(BLACK)
        display.rectangle(225, 175, 100, 25)
        display.set_pen(YELLOW)
        display.text(text, 225, 175, scale = 2)
        display.update()

def labelX(display, text = "Roll(1) ->"):    
        # clear previous label for Y button
        BLACK = display.create_pen(0, 0, 0)
        YELLOW = display.create_pen(255, 255, 0)
        display.set_pen(BLACK)
        display.rectangle(225, 50, 100, 25)
        display.set_pen(YELLOW)
        display.text(text, 225, 50, scale = 2)
        display.update()


# function for text at top of display (also game title at start)
def message(display, text = 'Shut The Box', x = 70, y = 0, scale = 3):
    BLACK = display.create_pen(0, 0, 0)
    WHITE = display.create_pen(255, 255, 255)
    # clear previous message
    display.set_pen(BLACK)
    display.rectangle(0, 0, 319, 45)
    # clear message area
    display.set_pen(WHITE)
    display.text(text, x, y, scale = scale)
    display.update()

# function to make a rectangle outline (rather than a filled rectangle)
def rect_outline(display, x, y, w, h, thickness = 1):
    display.line(x, y, (x + w - 1), y, thickness)
    display.line((x + w - 1), y, (x + w - 1), (y + h - 1), thickness)
    display.line(x, y, x, (y + h - 1), thickness)
    display.line(x, (y + h - 1), (x + w - 1), (y + h - 1), thickness)

# function to draw dice face
def dice(display, value, x, y): # x = 80 y = 90
    # clear previous dice
    BLACK = display.create_pen(0, 0, 0)
    display.set_pen(BLACK)
    display.rectangle(x, y, 52, 52)
    display.update()
    # dice outline
    WHITE = display.create_pen(255, 255, 255)
    display.set_pen(WHITE)
    rect_outline(display, x, y, 52, 52, 1)
    if value == 1:
        display.circle(x + 25, y + 25, 5)
    if value == 2:
        display.circle(x + 12, y + 38, 5) 
        display.circle(x + 40, y + 12, 5) 
    if value == 3:
        display.circle(x + 12, y + 38, 5) 
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
        
# function to create the numbered tiles to make it easier to make fine adjustments.
# this function has very limited flexibility.  It does NOT center the character or
# make sure it fits inside the outline.  This functionality could be added at a later time.
# The shift of 4 and 5 pixels in the x and y directions to place the character
# works for this application and could be adapted as needed.
def tile(display, myChar, x, y, w, h, thickness = 1, scale = 4, outCol = (255, 0, 255), charCol = (255, 0, 130)):
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
    

# function to roll 1 die
def rollOne(display, led):
    # turn on LED
    led.set_rgb(255, 0, 255)
    # roll one die
    die1 = randint(1, 6)
    dice(display, die1, 80, 150)
    rollTotal = die1
    # clear "Roll ="
    BLACK = display.create_pen(0, 0, 0)
    display.set_pen(BLACK)
    display.rectangle(225, 220, 95, 20)
    # display new "Roll ="
    YELLOW = display.create_pen(255, 255, 0)
    display.set_pen(YELLOW)
    display.text('Roll = ' + str(rollTotal), 225, 220, scale = 2)
    display.update()
    # turn off LED
    led.set_rgb(0, 0, 0)
    return rollTotal


def rollTwo(display, led):
    # turn on LED
    led.set_rgb(255, 0, 255)
    # roll two dice
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    dice(display, die1, 80, 150)
    dice(display, die2, 150, 150)
    rollTotal = die1+die2
    # clear "Roll ="
    BLACK = display.create_pen(0, 0, 0)
    display.set_pen(BLACK)
    display.rectangle(225, 220, 95, 20)
    # display new "Roll ="
    YELLOW = display.create_pen(255, 255, 0)
    display.set_pen(YELLOW)
    display.text('Roll = ' + str(rollTotal), 225, 220, scale = 2)
    display.update()
    # turn off LED
    led.set_rgb(0, 0, 0)
    return rollTotal


# display tiles - tiles in active have pink numbers; tiles not in active are grey
def tiles(display, active = [1, 2, 3, 4, 5, 6, 7, 8, 9]):
    for i in range(1, 10):
        if i in active:
            # numbers are pink
            tile(display, str(i), 30 * i, 85, 25, 40)
        else:
            # numbers are grey
            tile(display, str(i), 30 * i, 85, 25, 40, charCol = (128, 128, 128))



# rollCheck function will check roll to see if it is feasible to continue play
def rollCheck(rollTotal, availNums):
    # reduce availNums to all numbers <= dieTotal
    availNums = [x for x in availNums if x <= rollTotal]
    # create a variable for the length of availNums
    numsLen = len(availNums)
    # first check to see if a single number in availNums will work
    if rollTotal in availNums:
        return True
    # check sums of pairs of numbers in availNums if numsLen >= 2
    if numsLen >= 2: 
        for index1 in range(numsLen):
            for index2 in range(index1 + 1, numsLen):
                if sum([availNums[index1], availNums[index2]]) == rollTotal:
                    return True
    # check sums of three of numbers in availNums if numsLen >= 3
    if numsLen >= 3:
        for index1 in range(numsLen):
            for index2 in range(index1 + 1, numsLen):
                for index3 in range(index2 + 1, numsLen):
                    if sum([availNums[index1], availNums[index2],
                           availNums[index3]]) == rollTotal:
                        return True           
    # Only one combination of four numbers is less than the max roll of 12
    # 1+2+3+4 = 10, check just this case
    if rollTotal == 10 and all(x in availNums for x in [1, 2, 3, 4]):
        return True       
    # return False if none of the single numbers or possible sums from availNums will work 
    return False
    
    
    
    
    
    
    