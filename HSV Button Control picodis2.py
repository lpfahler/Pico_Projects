# Pico Display 2.0 Project:
# Display HSV color on RGB LED and Display; Adjust HSV Values with Buttons
# Lori Pfahler
# November 2023

# import modules
from utime import sleep
# If you have a Pico Display (smaller display) use DISPLAY_PICO_DISPLAY
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
from pimoroni import RGBLED, Button
# import my conversion functions
import hsv_rgb

# If you have a Pico Display (smaller display) use DISPLAY_PICO_DISPLAY
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)
display.set_backlight(1)

# set the font and make a black pen for clearing screen
display.set_font("bitmap8")
BLACK = display.create_pen(0, 0, 0)


# Initialize built-in RGB LED and four button switches
led = RGBLED(6, 7, 8)
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
# button_y = Button(15) # Not needed for this program

# function to clear screen from Pimoroni
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()

# set initial HSV color
hue = 0
sat = 1
value = 1
# convert HSV to RGB
red, green, blue = hsv_rgb.hsv2rgb(hue, sat, value)
# put color on RGB LED on display
led.set_rgb(red, green, blue)
# Create pen with RGB values
myColor = display.create_pen(red, green, blue) 
display.set_pen(myColor)
# Fill the screen with the color
display.clear()
# Set pen to black for text
display.set_pen(BLACK)    
display.text(f'Hue = {hue:<3d}', 100, 20, scale = 3)
display.text(f'Sat = {sat:<3.1f}', 100, 50, scale = 3)
display.text(f'Value = {value:<3.1f}', 100, 80, scale = 3)
display.text(f'R = {red:<3d}', 100, 120, scale = 3)
display.text(f'G = {green:<3d}', 100, 150, scale = 3)
display.text(f'B = {blue:<3d}', 100, 180, scale = 3)
display.update()

try:    
    while True:
        if button_a.read():
            # if a button press is detected then increase hue by 5 if < 359
            # if hue >= 360, hue = 0
            if hue >= 360:
                hue = 0
            else:
                hue += 5
        if button_b.read():
            # if b button press is detected then increase sat by 0.1 if < 1
            # if sat >= 1, sat = 0
            if sat >= 1:
                sat = 0
            else:
                sat += 0.1            
        if button_x.read():
            # if x button press is detected then increase value by 0.1 if < 1
            # if value >= 1, value = 0
            if value >= 1:
                value = 0
            else:
                value += 0.1
        # convert HSV to RGB
        red, green, blue = hsv_rgb.hsv2rgb(hue, sat, value)
        # put color on built-in RGB LED
        led.set_rgb(red, green, blue)
        # Create pen with converted HSV value
        myColor = display.create_pen(red, green, blue) 
        display.set_pen(myColor)
        # Fill the screen with the color
        display.clear()
        # Set pen to black for text
        display.set_pen(BLACK)
        display.text(f'Hue = {hue:<3d}', 100, 20, scale = 3)
        display.text(f'Sat = {sat:<3.1f}', 100, 50, scale = 3)
        display.text(f'Value = {value:<3.1f}', 100, 80, scale = 3)
        display.text(f'R = {red:<3d}', 100, 120, scale = 3)
        display.text(f'G = {green:<3d}', 100, 150, scale = 3)
        display.text(f'B = {blue:<3d}', 100, 180, scale = 3)
        display.update()

      
except KeyboardInterrupt:
    led.set_rgb(0, 0, 0)
    clear()
    display.set_backlight(0)



