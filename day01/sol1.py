#!/usr/bin/env python3

#
#advent of code 2018
#day 01
#part 1
#

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

freq = 0
for line in data:
    op = line[0]
    num = int(line[1:])
    if op == '+':
        freq += num
    elif op == '-':
        freq -= num
    else:
        print('wtf, op=',op)

print(freq)


