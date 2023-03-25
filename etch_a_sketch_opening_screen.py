# A program to draw the opening Etch-A-Sketch screen
# Lori Pfahler
# March 2023

# import modules
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

# setup I2C bus and display
i2c=I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
myOLED = SSD1306_I2C(128, 64, i2c, addr = 0x3c)
myOLED.init_display()


# Text centered
myOLED.text("Etch-A-Sketch", 10, 0)

# etch a sketch graphic
myOLED.rect(35, 15, 60, 40, 1)
myOLED.rect(45, 25, 40, 20, 1, True)
myOLED.ellipse(40, 47, 2, 2, 1, True)
myOLED.ellipse(88, 47, 2, 2, 1, True)
myOLED.show()

try:
    while True:
        pass
    
except KeyboardInterrupt:
    myOLED.fill(0)
    myOLED.show()
    