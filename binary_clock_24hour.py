# Program for a 24 hour Binary Clock (Military Time)
# Pico is plugged into your computer via a USB cable
# to get RTC (Real Time Clock)
# Lori Pfahler
# Feb 2023

from machine import Pin
import utime

# Hours (Orange):
# first digit, 0-2, two LEDs needed
hour1_1 = Pin(17, Pin.OUT)
hour1_2 = Pin(16, Pin.OUT)
# second digit, 0-9, four LEDs needed
hour2_1 = Pin(10, Pin.OUT)
hour2_2 = Pin(11, Pin.OUT)
hour2_4 = Pin(12, Pin.OUT)
hour2_8 = Pin(13, Pin.OUT)

# Minutes (Blue):
# first digit, 0-5, three LEDs needed
min1_1 = Pin(21, Pin.OUT)
min1_2 = Pin(20, Pin.OUT)
min1_4 = Pin(19, Pin.OUT)
# second digit, 0-9, four LEDs needed
min2_1 = Pin(6, Pin.OUT)
min2_2 = Pin(7, Pin.OUT)
min2_4 = Pin(8, Pin.OUT)
min2_8 = Pin(9, Pin.OUT)

# Seconds (Green):
# first digit - 0-5 - three LEDs needed
sec1_1 = Pin(28, Pin.OUT)
sec1_2 = Pin(27, Pin.OUT)
sec1_4 = Pin(26, Pin.OUT)
# second digit - 0-9 - four LEDs needed
sec2_1 = Pin(2, Pin.OUT)
sec2_2 = Pin(3, Pin.OUT)
sec2_4 = Pin(4, Pin.OUT)
sec2_8 = Pin(5, Pin.OUT)

utime.sleep(2)

# use try and except to turn LEDs off when exiting the program
try:
    while True:
        # get current time from computer (RTC = real time clock)
        # that the pico is connected to
        # localtime() returns an 8-tuple which contains:
        # (year, month, mday, hour, minute, second, weekday, yearday)
        currentTime = utime.localtime()
        # get digits for the hours
        hours = currentTime[3]
        if hours < 10:
            hour1Digit = 0
            hour2Digit = hours
        else:
            hour1Digit = int(str(hours)[0])
            hour2Digit = int(str(hours)[1])
        # first hour digit
        hour1Bin = '{0:02b}'.format(hour1Digit)
        hour1_2.value(int(hour1Bin[0]))
        hour1_1.value(int(hour1Bin[1]))
        # second hour digit
        hour2Bin = '{0:04b}'.format(hour2Digit)
        hour2_8.value(int(hour2Bin[0]))
        hour2_4.value(int(hour2Bin[1]))
        hour2_2.value(int(hour2Bin[2]))
        hour2_1.value(int(hour2Bin[3]))
        
        # get digits for the minutes
        minutes = currentTime[4]
        if minutes < 10:
            min1Digit = 0
            min2Digit = minutes
        else:
            min1Digit = int(str(minutes)[0])
            min2Digit = int(str(minutes)[1])
        # first minute digit
        min1Bin = '{0:03b}'.format(min1Digit)
        min1_4.value(int(min1Bin[0]))
        min1_2.value(int(min1Bin[1]))
        min1_1.value(int(min1Bin[2]))
        # second minute digit
        min2Bin = '{0:04b}'.format(min2Digit)
        min2_8.value(int(min2Bin[0]))
        min2_4.value(int(min2Bin[1]))
        min2_2.value(int(min2Bin[2]))
        min2_1.value(int(min2Bin[3]))
        
        # get digits for the seconds
        seconds = currentTime[5]
        if seconds < 10:
            sec1Digit = 0
            sec2Digit = seconds
        else:
            sec1Digit = int(str(seconds)[0])
            sec2Digit = int(str(seconds)[1])
        # first second digit
        sec1Bin = '{0:03b}'.format(sec1Digit)
        sec1_4.value(int(sec1Bin[0]))
        sec1_2.value(int(sec1Bin[1]))
        sec1_1.value(int(sec1Bin[2]))
        # second second digit
        sec2Bin = '{0:04b}'.format(sec2Digit)
        sec2_8.value(int(sec2Bin[0]))
        sec2_4.value(int(sec2Bin[1]))
        sec2_2.value(int(sec2Bin[2]))
        sec2_1.value(int(sec2Bin[3]))
    utime.sleep(0.25)
        
except KeyboardInterrupt:
    # turn off LEDs
    hour1_1.value(0)
    hour1_2.value(0)
    hour2_1.value(0)
    hour2_2.value(0)
    hour2_4.value(0)
    min1_1.value(0)
    min1_2.value(0)
    min1_4.value(0)
    min2_1.value(0)
    min2_2.value(0)
    min2_4.value(0)
    min2_8.value(0)
    sec1_1.value(0)
    sec1_2.value(0)
    sec1_4.value(0)
    sec2_1.value(0)
    sec2_2.value(0)
    sec2_4.value(0)
    sec2_8.value(0)