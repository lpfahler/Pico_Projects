# Pimon - building block program 1
# program to test component connections
# Lori Pfahler
# June 2023

# import modules
from machine import Pin, I2C, PWM
from utime import sleep, sleep_ms

# setup passive buzzer pim
buzzer = PWM(Pin(16))

# setup the four LEDs
redLED = Pin(14, Pin.OUT)
greenLED = Pin(12, Pin.OUT)
blueLED = Pin(10, Pin.OUT)
yellowLED = Pin(8, Pin.OUT)

# buzzer test DS4 at freq of 311Hz
buzzer.freq(311)
# use a duty cycle of 50% - can be set from 0 to 65535
buzzer.duty_u16(32768)
# hold the note
sleep(0.5)
# turn the sound off
buzzer.duty_u16(0)

# LED test
redLED.on()
sleep(1)
redLED.off()
greenLED.on()
sleep(1)
greenLED.off()
blueLED.on()
sleep(1)
blueLED.off()
yellowLED.on()
sleep(1)
yellowLED.off()