#!/usr/bin/env python3

#
#advent of code 2018
#day 11
#part 1
#

def sumsq(matrix, x0, y0):
    res = 0
    x1 = x0 + 3
    y1 = y0 + 3
    yo = y0
    while x0 < x1:
        y0 = yo
        while y0 < y1:
            res += matrix[x0][y0]
            y0 += 1
        x0 += 1
    return (res)


matrix = [[0 for x in range(300)] for y in range(300)]

puzzle_input =  5153

for y in range(300):
    for x in range(300):
        p = (x + 11) * (y + 1)
        p = (p + puzzle_input) * (x + 11)
        p = int((p / 100) % 10)
        p -= 5
        matrix[x][y] = p

res = 0
res_x = -1
res_y = -1

for y in range(0,300 - 3):
    for x in range(0,300 - 3):
        s = sumsq(matrix, x, y)
        if s > res:
            res = s
            res_x = x+1
            res_y = y+1

print('%d,%d' % (res_x, res_y))
