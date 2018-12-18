#!/usr/bin/env python3

import  copy
import  time
import  os

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

def print_game(data, i):
    os.system('clear')
    wooded_acres = 0
    lumberyards = 0
    for line in data:
        print(''.join(line))
        for sym in line:
            if sym == '|':
                wooded_acres += 1
            elif sym == '#':
                lumberyards += 1
    print()
    print('       round:', i)
    print('wooded_acres:', wooded_acres)
    print(' lumberyards:', lumberyards)
    print('      result:', wooded_acres * lumberyards)



def get_counts(data):
    wooded_acres = 0
    lumberyards = 0
    for line in data:
        for sym in line:
            if sym == '|':
                wooded_acres += 1
            elif sym == '#':
                lumberyards += 1
    return wooded_acres * lumberyards


with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

ldata = []
for line in data:
    ldata.append((list(line)))
data = ldata

i = 0
frames = []
while i < 2000:
    clone = copy.deepcopy(data)
    for y in range(len(data)):
        for x in range(len(data[y])):
            clone[y][x] = next_gen(data,y,x)
    data = clone
    i += 1
#
# logic is to capture one frame once they all have stabilized
# then break the loop next time it occurs
# and get value of n-th frame in the future
# not an elegant solution and it might fail on different input
# because some frames repeat more often than others
#
    if i >= 1000:
        count = get_counts(data)
        if i == 1000:
            saved_count = count
        if i > 1000 and count == saved_count:
            break
        frames.append(count)

r = (1000000000 - i) % len(frames)
print('result:',frames[r])

