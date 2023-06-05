# MicroPython Code for Formatting Output with format() Method
# Lori Pfahler
# June 2023


x = 12
y = 42.513978
my_string = "Lori's Robots"
print(f'x = {x}, y = {y}, My Channel = {my_string}')

print(f'x = {x:<10d}, y = {y:>10.3f}, My Channel = {my_string:^20s}')

# evaluating python expressions and using an object's methods
print(f'3x = {3*x}')

print(f'{my_string.upper()}')

print(f'{my_string.upper()} has a length of {len(my_string)}')


