#!/usr/bin/env python3

#
#advent of code 2018
#day 03
#part 2
#

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

d = {}
for line in data:
    sp = line.split(' ')
    _id = int(sp[0][1:])
    pos = sp[2][:-1].split(',')
    left = int(pos[0])
    top = int(pos[1])
    size = sp[3].split('x')
    wide = int(size[0])
    tall = int(size[1])
    d[_id] = [left, top, wide, tall]

matrix = [[0 for x in range(1000)] for y in range(1000)]
for k,v in d.items():
    x0 = v[0]
    x1 = v[0] + v[2]
    y1 = v[1] + v[3]
    while x0 < x1:
        y0 = v[1]
        while y0 < y1:
            if matrix[x0][y0] == 0:
                matrix[x0][y0] = 1
            elif matrix[x0][y0] != 0:
                matrix[x0][y0] = 2
            y0 += 1
        x0 += 1

for k,v in d.items():
    x0 = v[0]
    x1 = v[0] + v[2]
    y1 = v[1] + v[3]
    correct = True
    while x0 < x1:
        y0 = v[1]
        while y0 < y1:
            if matrix[x0][y0] != 1:
                correct = False
                break
            y0 += 1
        x0 += 1
        if not correct:
            break
    if correct:
        print(k)
        break
