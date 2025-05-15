# Bargraph (10 red LEDs) using network resistors (470 ohm)
# and a Potentiometer to turn the LEDs on and off
# like a volume control
#
# Lori Pfahler
# April 2025

import machine
import utime

# define pins for each LED -
# reverse order to make LEDs ordered the way I want
segments = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
segments_rev = reversed(segments)

# set up the GPIO pins as outputs
# LEDs = [machine.Pin(seg, machine.Pin.OUT) for seg in segments]
LEDs = [machine.Pin(seg, machine.Pin.OUT) for seg in segments_rev]

# set up potentiometer on ADC0, GPIO pin 26
pot = machine.ADC(26)

# function to scale x to y based on range of x and y
def scale(value, xmin, xmax, ymin, ymax):
    slope = (ymax - ymin)/(xmax - xmin)
    scaled_value = slope * (value - xmin) + ymin
    return scaled_value

try:
    while True:
        pot_value = pot.read_u16()
        level = int(scale(pot_value, 200, 65000, 0, 10))
        # print(level)
        for i in range(level):
            LEDs[i].on()
        for i in range(level, 10):
            LEDs[i].off()
        utime.sleep(0.05)

except KeyboardInterrupt:
    for i in range(10):
        LEDs[i].value(0)
    print("Done")

