# A program to demo drawing methods in frameBuffer library
# Not intended to run all together
# Copy and paste each section into the shell(REPL) and run
# section by section
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

# demo text
myOLED.text("Etch-A-Sketch!", 0, 0)
myOLED.text("Welcome to", 0, 16)
myOLED.text("Lori's Robots", 0, 32)
myOLED.show()

# demo fill()
myOLED.fill(1)
myOLED.show()

# demo .pixel()
myOLED.fill(0)
myOLED.pixel(0, 0, 1)
myOLED.pixel(20, 20, 1)
myOLED.pixel(20, 40, 1)
myOLED.pixel(20, 60, 1)
myOLED.show()

# demo blank line in yellow/blue display
# top is (0,0) to (15, 127) 16 pixels high
# bottom is (16, 0) to (63, 127) 48 pixels high
myOLED.fill(0)
myOLED.pixel(10, 15, 1)
myOLED.pixel(10, 16, 1)
myOLED.show()


# demo hline, vline and line
myOLED.fill(0)
myOLED.hline(5, 0, 127, 1)
myOLED.vline(50, 0, 63, 1)
myOLED.line(0,0, 127, 63, 1)
myOLED.show()


# demo retangle
myOLED.fill(0)
myOLED.rect(5, 20, 55, 30, 1)
# filled rectangle
myOLED.rect(70, 20, 30, 30, 1, True)
myOLED.show()


# demo circle and ellipse
myOLED.fill(0)
myOLED.ellipse(20, 16, 10, 10, 1)
# filled ellipse
myOLED.ellipse(80, 40, 40, 20, 1, True)
myOLED.show()