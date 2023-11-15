# HSV to RGB Conversion - Output to Shell
# Lori Pfahler
# November 2023

# import my conversion functions
import hsv2rgb


try:    
    while True:
        myChoice = input('Which Color Model Do You Want to Enter: HSV or RGB? ')
        if myChoice == 'HSV':
            # get hue, sat and value from user
            hue = float(input('Enter Hue (0-360)'))
            sat = float(input('Enter Saturation (0-1) '))
            value = float(input('Enter Value (0-1)'))
            red, green, blue = hsv_rgb.hsv2rgb(hue, sat, value)
            print('Converting HSV to RGB')
            print(f'Hue = {hue:3}, Saturation = {sat:3.1f}, Value = {value:3.1f}')
            print(f'R = {red:<3d}, G = {green:<3d}, B = {blue:<3d}')
            
        elif myChoice == 'RGB':
            # get red, green and blue values from user
            red = int(input('Enter Red (0-255)'))
            green = int(input('Enter Green (0-255)'))
            blue = int(input('Enter Blue (0-255)'))
            hue, sat, value = hsv_rgb.rgb2hsv(red, green, blue)
            print('Converting RGB to HSV')
            print(f'R = {red:<3d}, G = {green:<3d}, B = {blue:<3d}')
            print(f'Hue = {hue:3}, Saturation = {sat:3.1f}, Value = {value:3.1f}')
        
        else:
            print('Incorrent Entry - enter HSV or RGB')

except KeyboardInterrupt:
    print('Stop Program')