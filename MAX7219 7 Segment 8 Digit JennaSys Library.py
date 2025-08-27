# Using 8-Digit 7-Segment Display with MAX7219 Driver Chip
#
# Using JennaSys's library: https://github.com/JennaSys/micropython-max7219
# VCC to 3.3V rail
# GND Pin to GND rail
# DIN Pin to SPI0 TX - GP19
# CS Pin to SPI0 CSn - GP17
# CLK Pin to SPI0 SCK - GP18
#
# Starter Program - two displays 
#
# Lori Pfahler
# August 2025

from machine import Pin, SPI
import utime
import max7219

# set up the SPI bus
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19))
cs = Pin(17, Pin.OUT)

# set up the display - # digits is total number if daisy chaining displays
# scan_digits is the number of digits per module
display = max7219.SevenSegment(digits=16, scan_digits=8, cs=cs, spi_bus=0, reverse=True)

# send a number to the display
display.number(3.1415926)
utime.sleep(4)

# send a number to the display - won't display more than 7 digits with a decimal
display.number(3.141592653589793)
utime.sleep(4)

# send another number with a decimal to the display
display.number(123.456789123)
utime.sleep(4)

# send a 16 digit number to the display - No Decimal
display.number(1234567891234567)
utime.sleep(4)

# display a '1' (character) in position 3 using letter function
# doesn't clear display first
# clear the display
display.clear()
display.letter(3, '1')
utime.sleep(4)

# Scroll a message
display.message("Do you want to play a game?")
utime.sleep(0.5)

# Scroll faster
display.message("How about a nice game of chess?", delay = 0.15)
utime.sleep(0.5)

# text
display.text("Lori's Robots")
utime.sleep(10)

# clear the display
display.clear()

