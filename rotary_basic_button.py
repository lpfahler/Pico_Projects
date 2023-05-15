# Program to test the rotary encoder with button
# Lori Pfahler
# May 2023

# import modules
from utime import sleep, ticks_ms, sleep_ms
from machine import Pin
from rotary_irq_rp2 import RotaryIRQ

# setup rotary encoder
r = RotaryIRQ(pin_num_clk=12, 
              pin_num_dt=13)

# setup button on rotary encoder
myButton = Pin(11, Pin.IN, Pin.PULL_UP)

# define interrupt function for button
def selectLetter(myButton):
    global interruptFlag, debounceTime
    if (ticks_ms() - debounceTime) > 500:
        interruptFlag = 1
        debounceTime = ticks_ms()
        
# initialize IRQ
myButton.irq(trigger = Pin.IRQ_FALLING, handler = selectLetter)
interruptFlag=0
debounceTime=0

sleep(2)

valOld = r.value()
while True:
    if interruptFlag == 1:
        interruptFlag = 0
        print('button pressed')
    valNew = r.value()
    if valOld != valNew:
        valOld = valNew
        print(valNew)
sleep_ms(50)

