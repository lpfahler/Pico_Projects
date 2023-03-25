# Final program to create an Etch-A-Sketch with SSD1306 OLED Display
# and two potentionmeters as the dials
# This version includes reducing impact of noise in potentiometers
# using averaging, an opening screen, and a clear button
# Lori Pfahler
# March 2023

# import modules
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep
import framebuf

# setup I2C bus and display
i2c=I2C(0,sda = Pin(0), scl = Pin(1), freq = 400000)
myOLED = SSD1306_I2C(128, 64, i2c, addr = 0x3c)
myOLED.init_display()

# setup potentiometers on ADC pins: ADC0 and ADC1 
bluePot = machine.ADC(27)
greenPot = machine.ADC(26)

# setup button to clear the screen
myButton = Pin(15, Pin.IN, Pin.PULL_DOWN)

# define interrupt function for button
def clear_screen(myButton):
    global myOLED
    myOLED.fill(0)
    
# activate interrupt request
myButton.irq(trigger = Pin.IRQ_RISING, handler = clear_screen)

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

# opening screen
# Text centered
myOLED.text("Etch-A-Sketch", 10, 0)

# etch a sketch graphic
myOLED.rect(35, 15, 60, 40, 1)
myOLED.rect(45, 25, 40, 20, 1, True)
myOLED.ellipse(40, 47, 2, 2, 1, True)
myOLED.ellipse(88, 47, 2, 2, 1, True)
myOLED.show()
sleep(5)
myOLED.fill(0)



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
