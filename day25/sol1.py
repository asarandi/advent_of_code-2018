#!/usr/bin/env python3

import  sys

#
#advent of code 2018
#day 25
#part 1
#


# slow
#
#e1z4r6p21% time ./sol1.py input.txt
#422
#./sol1.py input.txt  139.43s user 0.57s system 99% cpu 2:20.91 total
#

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) + abs(a[3]-b[3])

def should_add_to_list(e, biglist):
    if len(biglist) == 0:
        return True
    for itm in biglist:
        if distance(e, itm) <= 3:
            return True
    return False

fn = 'input.txt'
if len(sys.argv) > 1:
    fn = sys.argv[1]

with open(fn) as fp:
    data = fp.read().splitlines()
    fp.close()

data = [[int(x) for x in line.split(',')] for line in data]

res = [[]]          #list of constellations
while len(data):
    flag = False
    for lst in res:
        for itm in data:
            if should_add_to_list(itm, lst) == True:
                lst.append(itm)
                flag = True
        for itm in lst:
            if itm in data:
                data.remove(itm)
    if flag == False:
        res.append([])

print(len(res))

