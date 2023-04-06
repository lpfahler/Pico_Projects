# Program to connect Pico W to WIFI and CheerLights
# displayed on an RGB LED
# Lori Pfahler
# April 2023

# import modules
import network
import socket
import urequests
import json
from picozero import RGBLED
from time import sleep

# SSID (Service Set Identifier = name of your wifi network)
# and password for your wifi network
# Fill in the next two lines
ssid = 'Your SSID here'
password = 'Your Wifi Password Here'

# function to connect to wifi
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

# function to get hex value for current CheerLights color
def getHexValue():
    urlHex = "http://api.thingspeak.com/channels/1417/field/2/last.json"
    r = urequests.get(urlHex)
    cheerlights = json.loads(r.content.decode('utf-8'))
    rgbColor = hex_to_rgb(cheerlights['field2'])
    r.close()
    return(rgbColor)

# function to get text value for current CheerLights color
def getTextValue():
    urlText = "http://api.thingspeak.com/channels/1417/field/1/last.json"
    r = urequests.get(urlText)
    cheerlightsText = json.loads(r.content.decode('utf-8'))
    rgbText = cheerlightsText['field1']
    r.close()
    return(rgbText)

# function to convert hex color format to RGB format
def hex_to_rgb(hexValue):
    hexColor= hexValue.lstrip('#')
    redValue = int(hexColor[0:2], 16)
    greenValue = int(hexColor[2:4], 16)
    blueValue = int(hexColor[4:6], 16)
    combinedValues = (redValue, greenValue, blueValue)
    return(combinedValues)

# setup RGB LED object
rgb = RGBLED(red=13, green=12, blue=11)

try:
    ip = connect()
    while True:
        print("Getting current color from CheerLights")
        # get the hexidecimal color value
        rgbColor = getHexValue()
        # get the text version of the color
        rgbText = getTextValue()
        print(rgbText, rgbColor)
        rgb.color = rgbColor
        # update every minute
        sleep(60)

    
except KeyboardInterrupt:
    # turn LED off
    rgb.off()

