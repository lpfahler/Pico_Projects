# A program to mock up Hangman game on 1306 Display

# Lori Pfahler
# May 2023

# import modules
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

# setup I2C bus and display
i2c=I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
myOLED = SSD1306_I2C(128, 64, i2c, addr = 0x3c)
myOLED.init_display()

# game title
myOLED.text("Hangman", 0, 0)
myOLED.show()

# letters not yet used
myOLED.text("ABCDEFG", 70, 10)
myOLED.text("HIJKLMN", 70, 20)
myOLED.text("OPQRSTU", 70, 30)
myOLED.text("VWXYZ", 78, 40)
myOLED.show()

# letter selector area
# this area will be controlled by the rotary encoder.  As the letter circles
# to the select area >A< if you press the button on the encoder, that letter
# will be guessed next.  The letter will become uppercase as it enters the
# selector window - will be lowercase when not in the window
myOLED.rect(77, 53, 41, 11, 1)
myOLED.text("->A<-", 78, 55)
myOLED.show()

# word area - can do up to 8 letter words
myOLED.text('A', 0, 55)
myOLED.text('B', 8, 55)
myOLED.text('C', 16, 55)
myOLED.text('D', 24, 55)
myOLED.text('E', 32, 55)
myOLED.text('F', 40, 55)
myOLED.text('G', 48, 55)
myOLED.text('H', 56, 55)

# blanks for letters
myOLED.hline(1, 63, 6, 1)
myOLED.hline(9, 63, 6, 1)
myOLED.hline(17, 63, 6, 1)
myOLED.hline(25, 63, 6, 1)
myOLED.hline(33, 63, 6, 1)
myOLED.hline(41, 63, 6, 1)
myOLED.hline(49, 63, 6, 1)
myOLED.hline(57, 63, 6, 1)
myOLED.show()

# show number of misses
myOLED.text('#Miss=10', 60, 0)
myOLED.show()

# hangman graphic parts that never change
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


# hangman parts
# head
myOLED.ellipse(36, 22, 3, 3, 1, True)
# body
myOLED.vline(36, 25, 15, 1)
# left arm
myOLED.hline(28, 30, 8, 1)
# right arm
myOLED.hline(37, 30, 8, 1)
# left leg
myOLED.line(36, 40, 28, 48, 1)
# right leg
myOLED.line(36, 40, 44, 48, 1)
# left hand
myOLED.rect(25, 29, 4, 3, 1, True)
# right hand
myOLED.rect(45, 29, 4, 3, 1, True)
# left foot
myOLED.rect(24, 47, 6, 3, 1, True)
# right fott
myOLED.rect(43, 47, 6, 3, 1, True)
myOLED.show()





