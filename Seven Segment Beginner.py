# Seven Segment Display Beginner Code 
# Light up each segment and then turn each off - top to bottom
# 220 ohm resistors for each segment
# Connect cathode pins to ground rail
#
# Lori Pfahler
# April 2025

import machine
import utime

# set up segments
a_LED = machine.Pin(13, machine.Pin.OUT) 
b_LED = machine.Pin(12, machine.Pin.OUT)  
c_LED = machine.Pin(18, machine.Pin.OUT)  
d_LED = machine.Pin(19, machine.Pin.OUT)  
e_LED = machine.Pin(16, machine.Pin.OUT)  
f_LED = machine.Pin(14, machine.Pin.OUT)  
g_LED = machine.Pin(15, machine.Pin.OUT)  
dp_LED = machine.Pin(17, machine.Pin.OUT) 

# set up delay times
delay_short = 1
delay_long = 2

while True:
    # turn on the segments - top to bottom
    a_LED.value(1)
    # print to shell segment status - use '\r' to replace the line
    print("Segment a on  ", end = '\r')
    utime.sleep(delay_short) 
    f_LED.value(1)
    print("Segment f on  ", end = '\r')
    utime.sleep(delay_short) 
    b_LED.value(1)
    print("Segment b on  ", end = '\r')
    utime.sleep(delay_short) 
    g_LED.value(1)
    print("Segment g on  ", end = '\r')
    utime.sleep(delay_short) 
    e_LED.value(1)
    print("Segment e on  ", end = '\r')
    utime.sleep(delay_short) 
    c_LED.value(1)
    print("Segment c on  ", end = '\r')
    utime.sleep(delay_short) 
    d_LED.value(1)
    print("Segment d on  ", end = '\r')
    utime.sleep(delay_short) 
    dp_LED.value(1)
    print("Segment dp on ", end = '\r')
    utime.sleep(delay_short) 
    
    utime.sleep(delay_long) 
    
    # turn off the segments bottom to top
    dp_LED.value(0)
    print("Segment dp off", end = '\r')
    utime.sleep(delay_short) 
    d_LED.value(0)
    print("Segment d off ", end = '\r')
    utime.sleep(delay_short) 
    c_LED.value(0)
    print("Segment c off ", end = '\r')
    utime.sleep(delay_short) 
    e_LED.value(0)
    print("Segment e off ", end = '\r')
    utime.sleep(delay_short) 
    g_LED.value(0)
    print("Segment g off ", end = '\r')
    utime.sleep(delay_short) 
    b_LED.value(0)
    print("Segment b off ", end = '\r')
    utime.sleep(delay_short) 
    f_LED.value(0)
    print("Segment f off ", end = '\r')
    utime.sleep(delay_short) 
    a_LED.value(0)
    print("Segment a off ", end = '\r')
    utime.sleep(delay_short) 

    utime.sleep(delay_long) 
