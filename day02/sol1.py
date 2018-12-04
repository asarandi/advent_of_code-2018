#!/usr/bin/env python3

#
#advent of code 2018
#day 02
#part 1
#

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

all_twos = 0
all_threes = 0
for line in data:
    twos = 0
    threes = 0
    for c in line:
        if line.count(c) == 2:
            twos = 1
        elif line.count(c) == 3:
            threes = 1
    all_twos += twos
    all_threes += threes

print(all_twos * all_threes)
