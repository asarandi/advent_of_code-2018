#!/usr/bin/env python3

from operator import itemgetter

#
#advent of code 2018
#day 23
#part 1
#


def distance(a, b):
    res = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
    return res

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

coords = []
for line in data:
    sp = line[5:].split('>')[0]
    r = int(line.split(', r=')[1])
    xyzr = []
    for item in sp.split(','):
        xyzr.append(int(item))
    xyzr.append(r)
    coords.append(xyzr)

coords = sorted(coords, key=itemgetter(3))
strong = coords[-1]

res = 0
#print(coords)
#print(strong)
for item in coords:
    d = distance(strong, item)
#    print('the nanobot at', item[:3], 'is distance', d, 'away')
    if d <= strong[3]:
        res += 1
print(res)

