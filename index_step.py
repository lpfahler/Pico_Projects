import utime

index = 0
step = 1
  
while True:
    if index == 12:  # 13 LEDS in my circuit
        step = -1
    elif index == 0:
        step = 1
    print('index =', index, 'step =', step)
    utime.sleep(1)
    index += step
