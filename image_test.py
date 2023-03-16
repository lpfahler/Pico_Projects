# Program to display an image on the display
# Image must be in PBM format - use GIMP software to create
# See YouTube video for instructions @lorisrobots
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

# open image file and read in as bytearray
# skip first three lines of file
with open('rpi_logo.pbm', 'rb') as file:
    file.readline() # format
    file.readline() # comment
    file.readline() # size of image
    data = bytearray(file.read())
    
myBuffer = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

# display image
myOLED.invert(1)
myOLED.blit(myBuffer, 0, 0)
myOLED.show()





















# for j in range(0,5):
#     if j == 0:
#         # scroll image to the right
#         for i in range(0, 25):
#             myOLED.scroll(1, 0)
#             myOLED.show()
#             sleep(0.001)
#     if j == 4:
#         for i in range(25, 0, -1):
#             myOLED.scroll(-1, 0)
#             myOLED.show()
#             sleep(0.001)
#     # scroll image to the right
#     if j > 0 and j < 4: 
#         for i in range(50, 0, -1):
#             myOLED.scroll(-1, 0)
#             myOLED.show()
#             sleep(0.001)
#         for i in range(0, 50, 1):
#             myOLED.scroll(1, 0)
#             myOLED.show()
#             sleep(0.001)
#         

    

  
    
