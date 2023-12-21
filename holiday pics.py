# Holiday Pics on the LED Matrix
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
display.set_brightness(0)

# change orientation to make it work as I wanted
display.set_angle(2).draw()

holiday_pics = {
    'xmas_tree' : b"\x02\x04\x1E\x00\x5A\x24\xFF\x81\x36\x48\x1E\x00\x04\x02\x00\x00",
    'wreath' : b"\x3C\x00\x3E\xC0\x47\xA8\x83\x70\x83\x70\x47\xA8\x3E\xC0\x3C\x00",
    'santa_hat' : b"\x00\x00\x02\x04\x02\x0C\x02\x1C\x02\x3C\x42\x1C\x02\x04\x00\x00",
    'stocking' : b"\x00\x00\x00\x00\x06\x00\x00\x06\x80\x7E\x80\x7C\x00\x00\x00\x00",
    'snow_flake': b"\x10\x00\x54\x00\x38\x00\xEE\x00\x38\x00\x54\x00\x10\x00\x00\x00",
    'present' : b"\x10\x00\x5E\x44\xDE\xC4\x3E\x3E\xDE\xC4\x5E\x44\x10\x00\x00\x00",
    'cane' : b"\x00\x00\x60\x00\x00\xC0\xC0\x00\x2A\xD4\x54\x2A\x00\x00\x00\x00",
}

# Display a custom pics on the LED
for pic in holiday_pics:
    display.set_icon(holiday_pics[pic]).draw()
    sleep(3)

# clear the display
display.fill(display.COLOUR_NONE).draw()

