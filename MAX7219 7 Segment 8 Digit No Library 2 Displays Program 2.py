# Using 8-Digit 7-Segment Display with MAX7219 Driver Chip
#
# No Library! TWO Displays, Add some helper functions Program 2
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

# send commands and values for two displays
# Must send No-Op command to display that is not being addressed (0x00, 0x00)
def send_cmd(address1, value1, address2, value2):
    CS.value(0)
    spi.write(bytes([address2, value2]))
    spi.write(bytes([address1, value1]))
    CS.value(1)
    
# blank/clear both displays
def clear():
    # clear first display
    for value in range(1, 9):
        send_cmd(value, 0x0F, 0x00, 0x0F)
    # clear second display
    for value in range(1, 9):
        send_cmd(0x00, 0x00, value, 0x0F)
        
# write test command off
send_cmd(0x0F, 0x00, 0x00, 0x00)
send_cmd(0x00, 0x00, 0x0F, 0x00)

# set normal operation
send_cmd(0x0C, 0x01, 0x00, 0x00)
send_cmd(0x00, 0x00, 0x0C, 0x01)

# enable all digits
send_cmd(0x0B, 0x07, 0x00, 0x00)
send_cmd(0x00, 0x00, 0x0B, 0x07)

# write brightness command - half brightness
send_cmd(0x0A, 0x07, 0x00, 0x00)
send_cmd(0x00, 0x00, 0x0A, 0x07)

# turn on decode mode for all digits
send_cmd(0x09, 0xFF, 0x00, 0x00)
send_cmd(0x00, 0x00, 0x09, 0xFF)

# clear display
clear()

# write the number "1" in digit 0 on second display
send_cmd(0x00, 0x00, 0x01, 0x01)

# write the number "2" in digit 1 on second display
send_cmd(0x00, 0x00, 0x02, 0x02)

# write the number "3" in digit 0 on first display
send_cmd(0x01, 0x03, 0x00, 0x00)

# write the number "4" in digit 1 on first display
send_cmd(0x02, 0x04, 0x00, 0x00)

utime.sleep(5)
clear()

try:
    while True:
        # count from 0 to 9 on first display in digit 0
        for i in range(10):
            send_cmd(0x01, i, 0x00, 0x00)
            utime.sleep(1)

    
except KeyboardInterrupt:
    # turn display off (shutdown mode)
    send_cmd(0x0C, 0x00, 0x00, 0x00)
    send_cmd(0x00, 0x00, 0x0C, 0x00)

