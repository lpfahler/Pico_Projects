# HSV <--> RGB Conversion Functions
# Lori Pfahler
# November 2023

# function to convert HSV color format to RGB color format

def hsv2rgb(hue, sat, value):
    # hue is expected to be between 0 and 360, sat: 0-1 and value: 0-1
    # the calculation below will make sure 360 deg is set to 0 deg
    hue = hue % 360
    
    # determine section for hue:
    # [0, 60) deg = section 0, [60, 120) deg = section 1 ... [300, 360) deg = section 5
    section = int(hue/60)
    
    # get min, max, range and slope for normalized RGB values (on 0-1 scale)
    maxRGB = value
    minRGB = value * (1 - sat)
    rangeRGB = value * sat
    slope = rangeRGB / 60
    
    # calculate normalize RGB values based on section of color wheel (0 to <360 degrees)
    
    # section 0 is [0, 60) degrees, R is max, G is increasing and B is min
    # (hue - 0) is how many degrees above 0 degrees (0 deg is the start of this section)
    if section == 0:
        Rnorm = maxRGB
        Gnorm = minRGB + (slope * (hue - 0.0))
        Bnorm  = minRGB
    # section 1 is [60, 120) degrees, R is decreasing, G is max and B is min
    # (hue - 60) is how many degrees above 60 degrees (60 deg is the start of this section)
    if section == 1:
        Rnorm = maxRGB - (slope * (hue - 60))
        Gnorm = maxRGB
        Bnorm  = minRGB
    # section 2 is [120, 180) degrees, R is min, G is max and B is increasing  
    if section == 2:
        Rnorm = minRGB
        Gnorm = maxRGB
        Bnorm  = minRGB + (slope * (hue - 120))       
    # section 3 is [180, 240) degrees, R is min, G is decreasing and B is max  
    if section == 3:
        Rnorm = minRGB
        Gnorm = maxRGB - (slope * (hue - 180))
        Bnorm  = maxRGB         
    # section 4 is [240, 300) degrees, R is increasing, G is min and B is max  
    if section == 4:
        Rnorm = minRGB + (slope * (hue - 240))
        Gnorm = minRGB 
        Bnorm  = maxRGB         
    # section 5 is [240, 300) degrees, R is max, G is min and B is decreasing  
    if section == 5:
        Rnorm = maxRGB
        Gnorm = minRGB 
        Bnorm  = maxRGB - (slope * (hue - 300))

# function to convert RGB color format to HSV color format
def rgb2hsv(R, G, B):
    # R, G and B are expected to be on 0-255 scale
    # normalize to 0-1 scale
    Rnorm = R / 255
    Gnorm = G / 255
    Bnorm = B / 255
    
    # get value and saturation, max
    maxRGB = max(Rnorm, Gnorm, Bnorm)
    value = maxRGB
    minRGB = min(Rnorm, Gnorm, Bnorm)
    if value == 0:
        sat = 0
    else:
        sat = 1 - (minRGB / value)

    # if maxRGB = minRGB then color is on white to black scale (i.e. greys in between)
    # hue = 0 deg and saturation = 0, value determines amount of grey
    # value = 1 is white, value = 0 is black
    if maxRGB == minRGB:
        hue = 0
        return(float(hue), float(sat), float(value))       
    if Rnorm == maxRGB and Bnorm == minRGB:
        # section 0; 0-60 degrees; slope positive
        deltaY = Gnorm - minRGB
        deltaX = 60*deltaY/(value*sat)
        hue = deltaX + 0
        return(float(hue), float(sat), float(value))       
    if Gnorm == maxRGB and Bnorm == minRGB:
        # section 1; 60-120; slope negative
        deltaY = Rnorm - minRGB
        deltaX = 60*deltaY/(value*sat)
        hue = 120 - deltaX
        return(float(hue), float(sat), float(value))       
    if Gnorm == maxRGB and Rnorm == minRGB:
        # section 2; 120-180; slope positive
        deltaY = Bnorm - minRGB
        deltaX = 60*deltaY/(value*sat)
        hue = deltaX + 120
        return(float(hue), float(sat), float(value))       
    if Bnorm == maxRGB and Rnorm == minRGB:
        # section 3; 180-240; slope negative
        deltaY = Gnorm - minRGB
        deltaX = 60*deltaY/(value*sat)
        hue = 240 - deltaX
        return(float(hue), float(sat), float(value))       
    if Bnorm == maxRGB and Gnorm == minRGB:
        # section 4; 240-360; slope positive
        deltaY = Rnorm - minRGB
        deltaX = 60*deltaY/(value*sat)
        hue = (deltaX + 240)
        return(float(hue), float(sat), float(value))       
    if Rnorm == maxRGB and Gnorm == minRGB:
        # section 5; 300-360 degrees; slope negative
        deltaY = Bnorm - minRGB
        deltaX = 60*deltaY/(value*sat)
        # to get 360 to return as 0 degrees
        hue = (360 - deltaX) % 360
        return(float(hue), float(sat), float(value