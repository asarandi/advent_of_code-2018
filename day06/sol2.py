#!/usr/bin/env python3

#
#advent of code 2018
#day 06
#part 2
#

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

d = {}
m = 0
i = 0
for line in data:
    line = line.split(',')
    x = int(line[0])
    y = int(line[1])
    if x > m: m = x
    if y > m: m = y
    d[i] = [x,y]
    i += 1

m += 1
res = 0
i = 0
while i < m:
    j = 0
    while j < m:
        dsum = 0
        for k,v in d.items():
            cd = abs(i-v[1]) + abs(j-v[0])
            dsum += cd
        if dsum < 10000:
            res += 1
        j += 1
    i += 1

print(res)
