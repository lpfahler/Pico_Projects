# Get individual digits for numbers from 0 to 9999
# Print to the shell
#
# Lori Pfahler
# May 2025

import utime

for i in range(10000):
    digit_ones = (i % 10) // 1
    digit_tens = (i % 100) // 10
    digit_hundreds = (i % 1000) // 100
    digit_thousands = (i % 10000) // 1000
    print(f'{digit_thousands}{digit_hundreds}{digit_tens}{digit_ones}', end = '\r')
    utime.sleep(0.5)
    