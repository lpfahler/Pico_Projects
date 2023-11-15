# Pico Display 2.0 Project:
# Rotate through HSV Color Wheel
# Lori Pfahler
# November 2023

# import modules
from utime import sleep
# If you have a Pico Display (smaller display) use DISPLAY_PICO_DISPLAY
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
from pimoroni import RGBLED
# import my conversion functions
import hsv_rgb

# If you have a Pico Display (smaller display) use DISPLAY_PICO_DISPLAY
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)
display.set_backlight(1)

display.set_font("bitmap8")
# WIDTH, HEIGHT = display.get_bounds()
BLACK = display.create_pen(0, 0, 0)
led = RGBLED(6, 7, 8)


try:    
    while True:
        for hue in range(0, 359, 5):
            myHSV = (hue, 1, 1)
            myRGB = hsv_rgb.hsv2rgb(myHSV[0], myHSV[1], myHSV[2])
            # put color on RGB LED and on display
            led.set_rgb(myRGB[0], myRGB[1], myRGB[2])
            # Create pen with converted HSV value
            myColor = display.create_pen(myRGB[0], myRGB[1], myRGB[2])  
            display.set_pen(myColor)
            # Fill the screen with the color
            display.clear()
            # Set pen to black
            display.set_pen(BLACK)
            # adjust scale and location of text on smaller pico display
            display.text(f'R = {myRGB[0]:<3d}', 100, 20, scale = 3)
            display.text(f'G = {myRGB[1]:<3d}', 100, 50, scale = 3)
            display.text(f'B = {myRGB[2]:<3d}', 100, 80, scale = 3)
            display.text(f'Hue = {myHSV[0]:<3d}', 100, 120, scale = 3)
            display.text(f'Sat = {myHSV[1]:<3d}', 100, 150, scale = 3)
            display.text(f'Value = {myHSV[2]:<3d}', 100, 180, scale = 3)
            display.update()
            sleep(1)
            
except KeyboardInterrupt:
    led.set_rgb(0, 0, 0)
    display.set_pen(BLACK)
    display.clear()
    display.update()
