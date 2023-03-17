# Program to calibrate the two potentiometers
# Lori Pfahler
# March 2023

# import modules
import machine
from utime import sleep

# setup potentiometers on ADC pins: ADC0 and ADC1
bluePot = machine.ADC(26)
greenPot = machine.ADC(27)

# function to get an average value for potentiometer
def read_pot(n, potName):
    potSum = 0
    for i in range(0, n):
        potSum = potName.read_u16() + potSum
        sleep(0.5)
    potAvg = potSum/n
    return(potAvg)
               
# read potentiometers for low value
goBlue = input('Turn Green and Blue Potentiometers to the LEFT and press <enter>')
greenLowAvg = read_pot(10, greenPot)
blueLowAvg = read_pot(10, bluePot)
print('Green Low Average =', greenLowAvg)
print('Blue Low Average =', blueLowAvg, '\n')
# read potentiometers for high value
goBlue = input('Turn Green and Blue Potentiometers to the RIGHT and press <enter>')
greenHighAvg = read_pot(10, greenPot)
blueHighAvg = read_pot(10, bluePot)
print('Green High Average =', greenHighAvg)
print('Blue High Average =', blueHighAvg)



