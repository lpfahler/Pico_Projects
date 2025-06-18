# Get individual digits for numbers from 0 to 9999
# Print to the shell - eliminate leading zeros
# Lori Pfahler
# May 2025

import utime

for i in range(10000):
    # get the digits in the ones, tens, hundreds, and thousands place
    digit_ones = (i % 10) // 1
    digit_tens = (i % 100) // 10
    digit_hundreds = (i % 1000) // 100
    digit_thousands = (i % 10000) // 1000
    # clear out leading zeros so they do not print
    if digit_thousands == 0:
        digit_thousands = ' '
        if digit_hundreds == 0:
            digit_hundreds = ' '
            if digit_tens == 0:
                digit_tens = ' '
    # print number by putting the digits back together
    print(f'{digit_thousands}{digit_hundreds}{digit_tens}{digit_ones}', end = '\r')
    # count slowly to watch
    utime.sleep(1)
    