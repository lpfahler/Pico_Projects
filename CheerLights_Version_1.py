# Program to connect Pico W to WIFI and get
# current CheerLights color printed to the shell
# Lori Pfahler
# April 2023

# import modules
import network
import socket
import urequests
import json
from time import sleep

# SSID (Service Set Identifier = name of your wifi network)
# and password for your wifi network
# Fill in the next two lines
ssid = 'Your SSID here'
password = 'Your Wifi Password Here'

# function to connect to wifi from Raspberry Pi Tutorial
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return(ip)

# function to convert hex color format to RGB format
def hex_to_rgb(hexValue):
    hexColor= hexValue.lstrip('#')
    print(hexValue, hexColor)
    redValue = int(hexColor[0:2], 16)
    greenValue = int(hexColor[2:4], 16)
    blueValue = int(hexColor[4:6], 16)
    print('Red =', redValue)
    print('Green =', greenValue)
    print('Blue =', blueValue)
    combinedValues = (redValue, greenValue, blueValue)
    return(combinedValues)

# CheerLights url for hex value of current color
url = "http://api.thingspeak.com/channels/1417/field/2/last.json"
ip = connect()
print("Getting current color from CheerLights")
r = urequests.get(url)
cheerlights = json.loads(r.content.decode('utf-8'))
rgbColor = hex_to_rgb(cheerlights['field2'])
print(rgbColor)
r.close()

