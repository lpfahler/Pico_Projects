# Program to create an Etch-A-Sketch with SSD1306 OLED Display
# and two potentionmeters as the dials - Part Two Version
# Lori Pfahler
# March 2023

# import modules
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep

# setup I2C bus and display
i2c=I2C(0,sda = Pin(0), scl = Pin(1), freq = 400000)
myOLED = SSD1306_I2C(128, 64, i2c, addr = 0x3c)
myOLED.init_display()

# setup potentiometers on ADC pins: ADC0 and ADC1 
bluePot = machine.ADC(27)
greenPot = machine.ADC(26)

# function to scale x data to y data based on min and max of each
def scale(value, xmin, xmax, ymin, ymax):
    slope = (ymax - ymin)/(xmax - xmin)
    scaled_value = slope * (value - xmin) + ymin
    return(scaled_value)

try:
    while True:
        # read potentiometers
        blueValue = bluePot.read_u16()
        greenValue = greenPot.read_u16()
        # green pot has a min of ~400 - scale to 4 to 123) to give a
        # border of four pixels - call this xpos
        xpos = int(scale(greenValue, 418, 65517, 4, 123))
        # blue pot has a min of ~500 - scale to 3, 61 to give a border
        # of three pixels to screen - call this ypos
        ypos = int(scale(blueValue, 419, 65473, 3, 61))
        # move pixel on screen   
        myOLED.pixel(xpos, ypos, 1)
        myOLED.show()
        # sleep just a little
        sleep(0.0001)

except KeyboardInterrupt:
    # clear screen
    myOLED.fill(0)
    myOLED.show()

