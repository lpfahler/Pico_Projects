# Program to create an Etch-A-Sketch with SSD1306 OLED Display
# and two potentionmeters as the dials
# This version includes two approaches to reduce
# the impact of noise in potentiometers: averaging and selective updating
# 
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

# function to get an average value for potentiometer
def read_pot(n, potName):
    potSum = 0
    for i in range(0, n):
        potSum = potName.read_u16() + potSum
    potAvg = potSum/n
    sleep(0.0001)
    return(potAvg)

# initialize variables to address noise in potentiometer readings
xposPrevious = int(scale(greenPot.read_u16(), 418, 65517, 4, 123))
yposPrevious = int(scale(bluePot.read_u16(), 419, 65473, 3, 61))

# adjust threshold
delta = 2

try:
    while True:
        # read potentiometers - use a running average of 10 values
        greenAvg = read_pot(10, greenPot)
        blueAvg = read_pot(10, bluePot)
        # scale to 4 to 123 to give a border of four pixels
        xpos = int(scale(greenAvg, 418, 65517, 4, 123))
        # scale to 3, 61 to give a border of three pixels to screen
        ypos = int(scale(blueAvg, 419, 65473, 3, 61))

        # change pos value only if it exceeds delta
        if abs(xpos - xposPrevious) < delta:
            xpos = xposPrevious
        if abs(ypos - yposPrevious) < delta:
            ypos = yposPrevious
            
        # move pixel on screen            
        # myOLED.pixel(xpos, ypos, 1)
        myOLED.ellipse(xpos, ypos, 1, 1, 1, True)
        myOLED.show()
        # sleep just a little
        sleep(0.0001)
        # update previous
        xposPrevious = xpos
        yposPrevious = ypos

except KeyboardInterrupt:
    # clear screen
    myOLED.fill(0)
    myOLED.show()

