# 8x8 LED Matrix Display - Show Arrow Graphic
# 
# Common Anode type: to light LED: row value = 1 and column value = 0
# 470 Ohm resistor for each column
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

pov_time_us = 1000
display_time_ms = 10000

# arrow graphic
# 1 = column off, 0 = column on for common anode (invert for cathode)
arrow = [
        [ 1, 1, 1, 1, 1, 1, 1, 1],
        [ 1, 1, 1, 0, 0, 0, 0, 1],
        [ 1, 1, 1, 1, 1, 0, 0, 1],
        [ 1, 1, 1, 1, 0, 1, 0, 1],
        [ 1, 1, 1, 0, 1, 1, 0, 1],
        [ 1, 1, 0, 1, 1, 1, 1, 1],
        [ 1, 0, 1, 1, 1, 1, 1, 1],
        [ 1, 1, 1, 1, 1, 1, 1, 1],
        ]

# show graphic for the display time
start = utime.ticks_ms()
while utime.ticks_diff(utime.ticks_ms(), start) < display_time_ms:
    for i in range(8):
        # set columns first to avoid carryover
        # credit to Keith Lohmeyer for the hint
        for j in range(8):
            columns[j].value(arrow[i][j])
        # turn on row
        rows[i].value(1)
        utime.sleep_us(pov_time_us)
        # turn off row
        rows[i].value(0)


    
