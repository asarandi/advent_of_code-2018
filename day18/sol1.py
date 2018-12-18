#!/usr/bin/env python3

import  copy

#
#advent of code 2018
#day 18
#part 1
#

def get_adjacent(data,y,x):
    res = []
    height = len(data)
    width = len(data[0])   
    if y > 0:
        res.append(data[y-1][x])
        if x > 0:
            res.append(data[y-1][x-1])
        if x + 1 < width:
            res.append(data[y-1][x+1])
    if x > 0:
        res.append(data[y][x-1])
    if x + 1 < width:
        res.append(data[y][x+1])
    if y + 1 < height:
        res.append(data[y+1][x])
        if x > 0:
            res.append(data[y+1][x-1])
        if x + 1 < width:
            res.append(data[y+1][x+1])
    return res

def next_gen(data,y,x):
    adj = get_adjacent(data,y,x)
    if data[y][x] == '.':               #rule 1
        if adj.count('|') >= 3:
            return '|'
        else:
            return '.'
    if data[y][x] == '|':               #rule 2
        if adj.count('#') >= 3:
            return '#'
        else:
            return '|'
    if data[y][x] == '#':               #rule 3
        if adj.count('#') >= 1 and adj.count('|') >= 1:
            return '#'
        else:
            return '.'
    return None

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

ldata = []
for line in data:
    ldata.append((list(line)))
data = ldata

minutes = 0
while minutes < 10:
    blank = [[' ' for x in range(len(data[0]))] for y in range(len(data))]
    clone = copy.deepcopy(data)
    for y in range(len(data)):
        for x in range(len(data[y])):
            clone[y][x] = next_gen(data,y,x)
    data = clone
    minutes += 1

wooded_acres = 0
lumberyards = 0
for line in data:
    print(''.join(line))
    for sym in line:
        if sym == '|':
            wooded_acres += 1
        elif sym == '#':
            lumberyards += 1
print('result', wooded_acres * lumberyards)

