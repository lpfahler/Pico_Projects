# A program to use rotary encoder to select letters
# display on OLED display - building block program
# for Hangman game

# Lori Pfahler
# May 2023

# import modules
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
from utime import sleep, sleep_ms, ticks_ms
from rotary_irq_rp2 import RotaryIRQ

# setup I2C bus and display
i2c=I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
myOLED = SSD1306_I2C(128, 64, i2c, addr = 0x3c)
myOLED.init_display()

# setup the rotary encoder
r = RotaryIRQ(pin_num_clk=12, 
              pin_num_dt=13, 
              min_val=1, 
              max_val=26,
              # when using half_step=True - need to use reverse = True
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
    if (ticks_ms() - debounceTime) > 500:
        # print('button pressed')
        interruptFlag = 1
        debounceTime = ticks_ms()
        
# initialize IRQ
myButton.irq(trigger = Pin.IRQ_FALLING, handler = selectLetter)

interruptFlag=0
debounceTime=0

# dictionary of letters
letters = { 1  : 'A', 2  : 'B', 3  : 'C', 4  : 'D', 5  : 'E', 6  : 'F', 7  : 'G',
            8  : 'H', 9  : 'I', 10 : 'J', 11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N',
            15 : 'O', 16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T', 21 : 'U',
            22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y', 26 : 'Z'}

# intialize variables and screen
valOld = r.value()

myOLED.rect(77, 53, 42, 11, 1)
myString = '->A<-'
myOLED.text(myString, 78, 55)
myOLED.show()

while True:
    valNew = r.value()
    if interruptFlag == 1:
        interruptFlag = 0
        print('letter selected is:', letters.get(valOld))
    if valOld != valNew:
        valOld = valNew 
        # clear the previous letter from the screen
        myOLED.rect(94, 55, 8, 8, 0, True)
        myOLED.show()
        print('Result =', valNew, 'Letter =', letters.get(valNew))
        # letter selector area - put in the correct letter
        myOLED.text(letters.get(valNew), 94, 55)
        myOLED.show()
   
        sleep_ms(50)