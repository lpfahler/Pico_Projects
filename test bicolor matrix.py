# Test Bi-Color Matrix from AdaFruit
#
# Adafruit Bicolor LED Square Pixel Matrix with I2C Backpack
# Product ID 902
# Matrix uses HT16K33 driver chip
# Using library from Smittytone @ github.com/smittytone/HT16K33-Python
#
# Lori Pfahler
# December 2023


# import modules
from utime import sleep
from machine import I2C, Pin

# need ht16k33.py and ht16k33matrixcolour.py in lib folder on pico
from ht16k33matrixcolour import HT16K33MatrixColour

# setup I2C bus
i2c = I2C(1, scl=Pin(15), sda=Pin(14))

# setup matrix 
display = HT16K33MatrixColour(i2c)
# set brightness: 0 (dim) to 15 (max brightness, default)
display.set_brightness(10)

# change orientation to make it work as I wanted
display.set_angle(2).draw()

# Fill display with each of the colours
#
#      Code from library ht16k33matrixcolour.py:
#      COLOUR_NONE = 0
#      COLOUR_GREEN = 2
#      COLOUR_RED = 1
#      COLOUR_YELLOW = 3

display.fill(display.COLOUR_RED).draw()

display.fill(ink = 2).draw()

display.fill(display.COLOUR_YELLOW).draw()

# clear the display
display.fill(ink = 0).draw()


# Turn on individual LEDs
# For this method - red and green are reversed!
# ink = 0 is none, ink = 1 is green, ink = 2 is red, ink = 3 is yellow

display.plot(0, 0, ink = 2).draw()
display.plot(7, 7, ink = 1).draw()

display.plot(0, 7, ink = 3).draw()
display.plot(7, 0, ink = 3).draw()

# clear the display
display.fill(ink = 0).draw()


# display some text
# ink = 0 is none, ink = 1 is red, ink = 2 is green, ink = 3 is yellow

message = 'Happy Holidays!'
display.scroll_text(message, ink = 1, paper = 0)
display.scroll_text(message, ink = 1, paper = 2)

# clear the display
display.fill(display.COLOUR_NONE).draw()
  
