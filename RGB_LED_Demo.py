# Demo program to use RGB LED with picozero module
# From picozero docs - April 2023
# Must install picozero on your Pico!
# in Thonny ... Tools menu ... Manage Packages ...
# search for picozero and Install

from picozero import RGBLED
from time import sleep

rgb = RGBLED(red=13, green=12, blue=11)

rgb.red = 255  # full red
sleep(1)
rgb.red = 128  # half red
sleep(1)

rgb.on() # white
sleep(1)

rgb.color = (0, 255, 0)  # full green
sleep(1)
rgb.color = (255, 0, 255)  # magenta
sleep(1)
rgb.color = (255, 255, 0)  # yellow
sleep(1)
rgb.color = (0, 255, 255)  # cyan
sleep(1)
rgb.color = (255, 255, 255)  # white
sleep(1)

rgb.color = (0, 0, 0)  # off
sleep(1)

# slowly increase intensity of blue
for n in range(255):
    rgb.blue = n
    sleep(0.05)
    
rgb.off()