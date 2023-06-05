# MicroPython Code for Formatting Output with format() Method
# Lori Pfahler
# June 2023


# Using positional arguments
print('x = {0}, y = {1}, My Channel = {2}'.format(12, 42.513978, "Lori's Robots"))

x = 12
y = 42.513978
my_string = "Lori's Robots"
print('x = {0}, y = {1}, My Channel = {2}'.format(x, y, my_string))


# Using named arguments
print('x = {x}, y = {y}, My Channel = {my_string}'.format(x = 12, y = 42.513978,
       my_string = "Lori's Robots"))

# align component < left justified, > right, ^ centered
x = 12
y = 42.513978
my_string = "Lori's Robots"
print('x = {0:<10d}, y = {1:>10.3f}, My Channel = {2:^20s}'.format(x, y, my_string))


# evaluating python expressions and using an object's methods
print('{0}'.format(x*3))

print('{0}'.format(my_string.upper()))

print('{0} has a length of {1}'.format(my_string.upper(), len(my_string)))

# binary
my_binary = 0b101111
z = 15
print('binary = {0:08b}'.format(my_binary))
print('binary = {0:b}'.format(z))

print('{0:b}, {0:#b}'.format(my_binary))
print('{0:b}, {0:#b}'.format(z))




