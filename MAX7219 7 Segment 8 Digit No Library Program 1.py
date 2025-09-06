# Using 8-Digit 7-Segment Display with MAX7219 Driver Chip
#
# No Library! Basics - Program 1, ONE display
#
# VCC to 5V rail
# GND Pin to GND rail
# DIN Pin to SPI0 TX - GP19
# CS Pin to SPI0 CSn - GP17
# CLK Pin to SPI0 SCK - GP18
#
# Lori Pfahler
# August 2025

from machine import Pin, SPI
import utime

# Control pins for display
DIN = Pin(19, Pin.OUT)
CLK = Pin(18, Pin.OUT)
CS = Pin(17, Pin.OUT)

# set up the SPI bus
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=CLK, mosi=DIN)

# initialize CS pin to high
CS.value(1)

# write test command - turn on
CS.value(0)
spi.write(bytes([0x0F, 0x01]))
CS.value(1)

utime.sleep(2)

# write test command off
CS.value(0)
spi.write(bytes([0x0F, 0x00]))
CS.value(1)

# set normal operation
CS.value(0)
spi.write(bytes([0x0C, 0x01]))
CS.value(1)

# enable all digits
CS.value(0)
spi.write(bytes([0x0B, 0x07]))
CS.value(1)

# write brightness command - full brightness
CS.value(0)
spi.write(bytes([0x0A, 0x0F]))
CS.value(1)

# turn on decode mode for all eight digits
CS.value(0)
spi.write(bytes([0x09, 0xFF]))
CS.value(1)



# write the number "1" in digit zero 
CS.value(0)
spi.write(bytes([0x01, 0x01]))
CS.value(1)

# write the number "2" in digit one 
CS.value(0)
spi.write(bytes([0x02, 0x02]))
CS.value(1)

# write the number "3" in digit two 
CS.value(0)
spi.write(bytes([0x03, 0x03]))
CS.value(1)

# write the number "4." in digit three with decimal point
CS.value(0)
spi.write(bytes([0x04, 0x84]))
CS.value(1)

# write a blank for digit four
CS.value(0)
spi.write(bytes([0x05, 0x0F]))
CS.value(1)

# write a blank for digit five
CS.value(0)
spi.write(bytes([0x06, 0x0F]))
CS.value(1)

# write a blank for digit six
CS.value(0)
spi.write(bytes([0x07, 0x0F]))
CS.value(1)

# write a blank for digit seven
CS.value(0)
spi.write(bytes([0x08, 0x0F]))
CS.value(1)

utime.sleep(5)



# switch to no decode
# no decode for all eight digits
CS.value(0)
spi.write(bytes([0x09, 0x00]))
CS.value(1)
   
# write a degree symbol in digit 0
CS.value(0)
spi.write(bytes([0x01, 0b01100011]))
CS.value(1)

# write a blank in digit 1 - 7
for i in range(2, 9):
    CS.value(0)
    spi.write(bytes([i, 0b00000000]))
    CS.value(1)

utime.sleep(5)

# turn display off (shutdown mode)
CS.value(0)
spi.write(bytes([0x0C, 0x00]))
CS.value(1)

