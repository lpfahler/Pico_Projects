import machine
# utime and time are the same - the time library just points to utime library
from utime import sleep

# on regular pico can use GP25 - on pico w use 'LED"
#  for regular pico use: internalLED = machine.Pin(25, machine.Pin.OUT
internalLED = machine.Pin('LED', machine.Pin.OUT)

myList = [1.0, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30,0.20, 0.10,
          0.05, 0.04, 0.03, 0.02, 0.019, 0.018, 0.017, 0.016, 0.015,
          0.014, 0.013, 0.012, 0.011, 0.010]
while True:
    for num in myList: 
        if num >= 0.5:
            # blink 5 times
            for nBlinks in range(0, 5):
                print('Can you see this speed? ', num, 'seconds')
                internalLED.toggle()
                sleep(num)
        elif num >= 0.1 and num < 0.5:
            # blink 10 times
            for nBlinks in range(0, 10):
                print('Can you see this speed? ', num, 'seconds')
                internalLED.toggle()
                sleep(num)
        else: 
            # blink 50 times
            for nBlinks in range(0, 50):
                print('Can you see this speed? ', num, 'seconds')
                internalLED.toggle()
                sleep(num)