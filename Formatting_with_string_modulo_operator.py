# MicroPython Code for Formatting Output with String Modulo Operator
# Lori Pfahler
# June 2023


x = 12
y = 42.513978
my_string = "Lori's Robots"

# basic output to shell
# print function arguments 'sep' and 'end'
# defaults are sep = ' ' and end = '\n'

print(x, y, my_string)

print(x, y, my_string, sep = ', ')

print('x =', x, 'y =', y, 'My Channel =', my_string)

# end = '\r' useful for printing to shell to monitor status of a sensor
# and not filling up the screen

from utime import sleep
for i in range(11):
    print(i, end = '\r')
    sleep(1)
    
# useful string methods

print(my_string)

print(my_string.lower())

print(my_string.upper())



# controlling number format

print('x =', x, 'y =', round(y, 3))

print('x = %d, y = %f, My Channel = %s' %(x, y, my_string))



print('x = %.1f, y = %.3f' %(x, y))

print('x = %6.1f, y = %6.3f' %(x, y))

# exponential format

z = 0.0006298

print('z = %8.2e' %z, 'z = %8.2E' %z)

# binary as a string

my_binary = 0b101111

print('binary = %s' %bin(my_binary)[2:])

