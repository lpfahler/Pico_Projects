# Get Data from Photoresitor
# Photoresistor is connected to power rail on one leg
# and through voltage divider on the other leg (using 10K Ohm
# resistor connected to ground) to ADC pin on pico (ADC0 in this program) 
#
# Lori Pfahler
# May 2025

import machine
import utime

# set up photoresistor on ADC0, GPIO pin 26
photoresist = machine.ADC(26)


try:
    while True:
        # read_u16() returns a value between 0 and 65535
        # light_value is percent of total possible from photoresitor value
        photo_value = photoresist.read_u16()
        light_value = (photo_value / 65535) * 100
        # use fstring to format data to two decimal places
        print(f'{photo_value}, {light_value:5.2f}%')
        utime.sleep(1)

except KeyboardInterrupt:
    print("Done")
