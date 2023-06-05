# MicroPython code to demonstrate printing output from sensor
# Uses onboard temperature sensor for Pico/Pico W
# Lori Pfahler
# June 2023

# import modules
from machine import ADC
from utime import sleep

# setup ADC pin for onboard temperature sensor
adcPin = machine.ADC(4)


while True:
    result = adcPin.read_u16()
    # conversion provided in Raspberry Pi documentation
    voltage = result * (3.3 / (65535))
    tempC = 27 - (voltage - 0.706)/0.001721
    # create deg F version as well
    tempF = 32 +( 1.8 * tempC)
    # simple print without any formatting
    # print('Temperature in degC =', tempC, 'in degF =', tempF)
    
    # use of end option in print function
    # print('Temperature in degC =', tempC, 'in degF =', tempF, end = '\r')
    
    # use of sep argument in print function
    # print('Temperature in degC = ', round(tempC, 1), ', in degF = ', round(tempF, 1), sep='')
    
    # use of string modulo operator
    # print('Temperature in degC = %4.1f, in degF = %5.1f' %(tempC, tempF))
    
    # use of format() method
    # print('Temperature in degC = {0}, in degF = {1}'.format(tempC, tempF))
    # print('Temperature in degC = {0:4.1f}, in degF = {1:5.1f}'.format(tempC, tempF))
    
    # use of f strings
    # print(f'Temperature in degC = {tempC}, in degF = {tempF}')
    print(f'Temperature in degC = {tempC:4.1f}, in degF = {tempF:5.1f}', end = '\r')
    
    sleep(2)