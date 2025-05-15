# Bargraph (10 red LEDs) using network resistors (470 ohm)
# and ten GPIO pins for control
#
# Lori Pfahler
# April 2025

import machine
import utime

# define pins for each LED
segments = (6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
# set up the GPIO pins as outputs
LEDs = [machine.Pin(seg, machine.Pin.OUT) for seg in segments]

try:
    while True:
        for i in range(10):
           LEDs[i].toggle()
           utime.sleep(0.2)

except KeyboardInterrupt:
    for i in range(10):
        LEDs[i].value(0)
    print("Done")

