# Program to turn an LED on and off with a Button (momentary switch)
# using an interrupt and debouncing
# Lori Pfahler
# Feb 2023

# import modules
from machine import Pin
import utime

# setup button and LED pins
myButton = Pin(0, Pin.IN, Pin.PULL_DOWN)
myLED = Pin(1, Pin.OUT)

# variables to track interrupt activation and time for debouncing
interrupt_flag = 0
debounce_time = 0

# interrupt function
def button_handler(myButton):
    global interrupt_flag, debounce_time
    if (utime.ticks_ms()-debounce_time) > 300:
        interrupt_flag = 1
        debounce_time=utime.ticks_ms()

# interrupt request
myButton.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

while True:
    # turn on/off LED when the button is pressed
    if interrupt_flag == 1:
        interrupt_flag = 0
        print("Interrupt Detected")
        myLED.toggle()
