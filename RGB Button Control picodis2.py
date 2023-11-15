# Pico Display 2.0 Project:
# Display RGB color on RGB LED and Display; Adjust RGB Values with Buttons
# Lori Pfahler
# November 2023

# import modules
from utime import sleep
# If you have a Pico Display (smaller display) use DISPLAY_PICO_DISPLAY
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
from pimoroni import RGBLED, Button

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

# set initial RGB color
red = 255
green = 0
blue = 0
# put color on RGB LED on display
led.set_rgb(red, green, blue)
# Create pen with RGB values
myColor = display.create_pen(red, green, blue) 
display.set_pen(myColor)
# Fill the screen with the color
display.clear()
# Set pen to black for text
display.set_pen(BLACK)    
display.text(f'R = {red:<3d}', 100, 50, scale = 4)
display.text(f'G = {green:<3d}', 100, 90, scale = 4)
display.text(f'B = {blue:<3d}', 100, 130, scale = 4)
display.update()

try:    
    while True:
        if button_a.read():
            # if a button press is detected then increase red by 5 if < 255
            # if red >= 255, red = 0
            if red >= 255:
                red = 0
            else:
                red += 5
        if button_b.read():
            # if b button press is detected then increase green by 5 if < 255
            # if green >= 255, green = 0
            if green >= 255:
                green = 0
            else:
                green += 5            
        if button_x.read():
            # if x button press is detected then increase blue by 5 if < 255
            # if blue >= 255, blue = 0
            if blue >= 255:
                blue = 0
            else:
                blue += 5 
        # put color on built-in RGB LED
        led.set_rgb(red, green, blue)
        # Create pen with converted HSV value
        myColor = display.create_pen(red, green, blue) 
        display.set_pen(myColor)
        # Fill the screen with the color
        display.clear()
        # Set pen to black for text
        display.set_pen(BLACK)    
        display.text(f'R = {red:<3d}', 100, 50, scale = 4)
        display.text(f'G = {green:<3d}', 100, 90, scale = 4)
        display.text(f'B = {blue:<3d}', 100, 130, scale = 4)
        display.update()

      
except KeyboardInterrupt:
    led.set_rgb(0, 0, 0)
    clear()
    display.set_backlight(0)


