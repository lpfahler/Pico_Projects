# 8x8 LED Matrix Display - Show a Message
# Message = "Lori's Robots"
#
# Common Anode type: to light LED: row value = 1 and column value = 0
# 470 Ohm resistor for each column
#
# template for characters: https://xantorohara.github.io/led-matrix-editor/
#
# Lori Pfahler
# July 2025

from machine import Pin
import utime

# rows of matrix
row1 = machine.Pin(16, machine.Pin.OUT)
row2 = machine.Pin(18, machine.Pin.OUT)
row3 = machine.Pin(15, machine.Pin.OUT)
row4 = machine.Pin(17, machine.Pin.OUT)
row5 = machine.Pin(11, machine.Pin.OUT)
row6 = machine.Pin(14, machine.Pin.OUT)
row7 = machine.Pin(12, machine.Pin.OUT)
row8 = machine.Pin(13, machine.Pin.OUT)

# columns of matrix
col1 = machine.Pin(2, machine.Pin.OUT)
col2 = machine.Pin(3, machine.Pin.OUT)
col3 = machine.Pin(4, machine.Pin.OUT)
col4 = machine.Pin(5, machine.Pin.OUT)
col5 = machine.Pin(6, machine.Pin.OUT)
col6 = machine.Pin(7, machine.Pin.OUT)
col7 = machine.Pin(8, machine.Pin.OUT)
col8 = machine.Pin(9, machine.Pin.OUT)

# row list
rows = [row1, row2, row3, row4, row5, row6, row7, row8]
# column list
columns = [col1, col2, col3, col4, col5, col6, col7, col8]

# set all columns to high
for col in columns:
    col.value(1)
# set all rows to low
for row in rows:
    row.value(0)

# function to show graphic for the display time
def show_graphic(graphic, pov_time, display_time):
    start = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start) < display_time:
        for i in range(8):
            # set columns first to avoid carryover
            for j in range(8):
                columns[j].value(graphic[i][j])
            # turn on row
            rows[i].value(1)
            utime.sleep_us(pov_time)
            # turn off row
            rows[i].value(0)

# letters/characters needed for message:
# 1 = column off, 0 = column on for common anode display (invert for cathode)

blank = [
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    ]

l_upper = [
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 0, 0, 0, 0, 1],
    ]

o_lower = [
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 0, 0, 0, 0, 1, 1],
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, 1, 0, 0, 0, 0, 1, 1],
    ]

r_lower = [
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 0, 0, 0, 1, 1],
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    ]
    
i_lower = [
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 0, 0, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 0, 0, 1, 1, 1],
    [ 1, 1, 1, 0, 0, 1, 1, 1],
    [ 1, 1, 1, 0, 0, 1, 1, 1],
    [ 1, 1, 0, 0, 0, 0, 1, 1],
    ]
 
single_quote = [
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 0, 0, 1, 1, 1, 1],
    [ 1, 1, 0, 0, 1, 1, 1, 1],
    [ 1, 1, 0, 0, 1, 1, 1, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    
s_lower = [
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 0, 0, 0, 0, 0, 1],
    [ 1, 0, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 0, 0, 0, 0, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 0, 1],
    [ 1, 0, 0, 0, 0, 0, 1, 1],
    ]
    
r_upper = [
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 0, 0, 0, 1, 1],
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, 0, 0, 0, 0, 0, 1, 1],
    [ 1, 0, 0, 0, 0, 1, 1, 1],
    [ 1, 0, 0, 1, 0, 0, 1, 1],
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    ]

b_lower = [
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 1, 1, 1, 1, 1],
    [ 1, 0, 0, 0, 0, 0, 1, 1],
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, 0, 0, 1, 1, 0, 0, 1],
    [ 1, 0, 0, 0, 0, 0, 1, 1],
    ]

t_lower = [
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 0, 0, 1, 1, 1],
    [ 1, 1, 1, 0, 0, 1, 1, 1],
    [ 1, 0, 0, 0, 0, 0, 0, 1],
    [ 1, 1, 1, 0, 0, 1, 1, 1],
    [ 1, 1, 1, 0, 0, 1, 1, 1],
    [ 1, 1, 1, 0, 0, 1, 1, 1],
    ]
    
# "Lori's Robots" message to display
message = [l_upper, o_lower, r_lower, i_lower, single_quote, s_lower, blank,
           r_upper, o_lower, b_lower, o_lower, t_lower, s_lower]

try:
    while True:
        for char in message:
            show_graphic(char, 1000, 200)
        utime.sleep(1)

except:
    # set all columns to high
    for col in columns:
        col.value(1)
    # set all rows to low
    for row in rows:
        row.value(0)   

