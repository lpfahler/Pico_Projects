# Program to test the rotary encoder
# Lori Pfahler
# May 2023

# import modules
from utime import sleep, sleep_ms
from rotary_irq_rp2 import RotaryIRQ

# setup rotary encoder
r = RotaryIRQ(pin_num_clk=12, 
              pin_num_dt=13)

sleep(2)

valOld = r.value()
while True:
    valNew = r.value()
    if valOld != valNew:
        valOld = valNew
        print(valNew)
    sleep_ms(50)