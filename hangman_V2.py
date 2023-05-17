# A program to use a rotary encoder to play
# Hangman on an OLED SSD1306 display
# Lori Pfahler
# May 2023


# import modules
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
from utime import sleep, sleep_ms, ticks_ms
from rotary_irq_rp2 import RotaryIRQ
from random import randint
from word_list import *

# setup I2C bus and display
i2c=I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
myOLED = SSD1306_I2C(128, 64, i2c, addr = 0x3c)
myOLED.init_display()

# setup the rotary encoder
r = RotaryIRQ(pin_num_clk=12, 
              pin_num_dt=13, 
              min_val=1, 
              max_val=26,
              # when using half_step = True - need to use reverse = True
              # not clear why that is needed
              reverse=True,
              # need to use half_step=True to get a change for each indent in my KY-040
              half_step = True,
              range_mode=RotaryIRQ.RANGE_WRAP)

# setup button on rotary encoder
myButton = Pin(11, Pin.IN, Pin.PULL_UP)

# define interrupt function for button
def selectLetter(myButton):
    global interruptFlag, debounceTime
    if (ticks_ms() - debounceTime) > 300:
        # print('button pressed')
        interruptFlag = 1
        debounceTime = ticks_ms()
        
# initialize IRQ
myButton.irq(trigger = Pin.IRQ_FALLING, handler = selectLetter)
interruptFlag=0
debounceTime=0

# dictionary of letters for rotary encoder input
letters = { 1  : 'A', 2  : 'B', 3  : 'C', 4  : 'D', 5  : 'E', 6  : 'F', 7  : 'G',
            8  : 'H', 9  : 'I', 10 : 'J', 11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N',
            15 : 'O', 16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T', 21 : 'U',
            22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y', 26 : 'Z'}

# function for randomly selecting the word length and word
def getWord():
    global ALLWORDS
    # randomly select wordLength - may allow user to input in the future
    wordLength = randint(4, 8)
    listIndex = wordLength - 4
    randIndex = randint(0, len(ALLWORDS[listIndex]) - 1)
    return ALLWORDS[listIndex][randIndex]

# function to draw the blanks needed for the word
def drawBlanks(wordLength):
    startBlank = [1, 9, 17, 25, 33, 41, 49, 57]
    # printing to see it work - remove once program complete
    print(wordLength)
    for i in range(0, wordLength):
        myOLED.hline(startBlank[i], 63, 6, 1)
    myOLED.show()

# function concatenate and split up letAvail list for printing to display
def show_letAvail(letList, display):
    display.rect(70, 10, 58, 40, 0, True)
    display.text((''.join(letList[0:7])), 70, 10)
    display.text((''.join(letList[7:14])), 70, 20)
    display.text((''.join(letList[14:21])), 70, 30)
    display.text((''.join(letList[21:26])), 78, 40)
    display.show()

# function for printing hangman parts
def hangman(n):
    if n == 1:
        # head
        myOLED.ellipse(36, 22, 3, 3, 1, True)
        myOLED.show()
    if n == 2:       
        # body
        myOLED.vline(36, 25, 15, 1)
        myOLED.show()
    if n == 3:
        # left arm
        myOLED.hline(28, 30, 8, 1)
        myOLED.show()
    if n == 4:
        # right arm
        myOLED.hline(37, 30, 8, 1)
        myOLED.show()
    if n == 5:
        # left leg
        myOLED.line(36, 40, 28, 48, 1)
        myOLED.show()
    if n == 6:
        # right leg
        myOLED.line(36, 40, 44, 48, 1)
        myOLED.show()
    if n == 7:
        # left hand
        myOLED.rect(25, 29, 4, 3, 1, True)
        myOLED.show()
    if n == 8:
        # right hand
        myOLED.rect(45, 29, 4, 3, 1, True)
        myOLED.show()
    if n == 9:
        # left foot
        myOLED.rect(24, 47, 6, 3, 1, True)
        myOLED.show()
    if n == 10:
        # right foot
        myOLED.rect(43, 47, 6, 3, 1, True)
        myOLED.show()

# function to show current number of misses
def show_n_misses(n):
    # clear the area
    myOLED.rect(60, 0, 67, 8, 0, True)
    myOLED.show()
    # show the number of guesses
    missString = "#Miss="+str(n)
    myOLED.text(missString, 60, 0)
    myOLED.show()
    
    
#### Main Program ####

try:
 while True:
    # game title
    myOLED.text("Hangman", 0, 0)
    myOLED.show()

    # hangman graphic parts shown at the start of the game
    # vertical bar
    myOLED.rect(5, 12, 2, 40, 1)
    # horizontal bar
    myOLED.rect(5, 12, 31, 2, 1)
    # crossbar
    myOLED.line(5, 25, 18, 12, 1)
    # rope
    myOLED.rect(36, 12, 2, 6, 1)
    # ground
    myOLED.rect(0, 52, 64, 2, 1)
    myOLED.show()

    # initialize available letters list
    letAvail = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H' ,'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    # put letters available on the screen for the first time
    show_letAvail(letAvail, myOLED)

    # put "letter select area" on screen - start with A
    myOLED.rect(77, 53, 42, 11, 1)
    firstString = '->A<-'
    myOLED.text(firstString, 78, 55)
    myOLED.show()

    # randomly choose word length (4-8 letters) and select word
    selectedWord = getWord()
    print(selectedWord)
    # letters in the selectedWord
    letWord = list(selectedWord)
    print(letWord)

    # draw blanks for selected word
    drawBlanks(len(selectedWord))
    # starting pixels for letters over the blanks
    letStart = [0, 8, 16, 24, 32, 40, 48, 56]

    # select maximum number of guesses allowed based on word length
    if len(selectedWord) < 7:
        maxGuess = 6
    else:
        maxGuess = 10

    # intialize number of misses
    nMiss = 0
    # show number of guesses
    show_n_misses(nMiss)
    
    # intialize valOld for selecting letters via rotary encoder
    valOld = r.value()

    # initialize selLetter to blank
    selLetter = ''
    # intialize stopFlag
    stopFlag = 0
    # initialize nCorrect
    nCorrect = 0

    while (stopFlag == 0):
        # read rotary encoder
        valNew = r.value()
        # check to see if button is pressed
        if interruptFlag == 1:
            interruptFlag = 0
            selLetter = letters.get(valNew)
            print('letter selected is:', selLetter)
            if selLetter in letAvail:         
                # replace selected letter with a blank in letAvail list 
                letAvail = [' ' if i == selLetter else i for i in letAvail]
                # show the letters available after the most recent selection
                show_letAvail(letAvail, myOLED)
                print(letAvail)
                # if selLetter is in letWord, find the index(es) and print to screen
                if selLetter.lower() in letWord:
                    # list comprehension to get index value(s) of letters found in letWord
                    findex = [i for i, letter in enumerate(letWord) if letter == selLetter.lower()]
                    print(findex)
                    for i in findex:             
                        myOLED.text(selLetter, letStart[i], 55)
                        myOLED.show()
                    # update nCorrect
                    nCorrect += len(findex)
                else:
                    # this code runs if the letter was not found
                    print('letter not found')
                    nMiss +=1
                    # add the next part of the hangman
                    hangman(nMiss)
                    print(nMiss)
                    show_n_misses(nMiss)
                    if nMiss == maxGuess:
                        # end game if maxGuess has been used
                        myOLED.rect(60, 0, 68, 8, 0, True)
                        myOLED.show()
                        myOLED.text("Sorry", 60, 0)
                        # show the word
                        myOLED.text(selectedWord.upper(), 0, 55)
                        myOLED.show()
                        stopFlag = 1
            else:
                # this code runs if the user selects a letter that has already been used
                print('repeat selection')
                myOLED.rect(60, 0, 68, 8, 0, True)
                myOLED.show()
                myOLED.text("Repeat", 60, 0)
                myOLED.show()
                sleep(2)
                show_n_misses(nMiss)
        if nCorrect == len(letWord):
            # check to see if user has correctly guessed the word
            stopFlag = 1
            myOLED.rect(60, 0, 68, 8, 0, True)
            myOLED.show()
            myOLED.text("Winner!", 60, 0)
            myOLED.show()
            
        # check if user has moved rotary encoder
        if valOld != valNew:
            valOld = valNew 
            # clear the previous letter from the screen
            myOLED.rect(94, 55, 8, 8, 0, True)
            myOLED.show()
            # get the new letter
            displayLetter = letters.get(valNew)  
            # display new letter on the screen
            myOLED.text(displayLetter, 94, 55)
            myOLED.show()  
            sleep_ms(50)
            
    # sleep to allow time to see the final results; then clear and start again
    sleep(5)
    myOLED.fill(0)
    myOLED.show()
    
except KeyboardInterrupt:
    myOLED.fill(0)
    myOLED.show()
