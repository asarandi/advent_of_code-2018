#!/usr/bin/env python3

#
#advent of code 2018
#day 01
#part 2
#

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

seen = set()
freq = 0
seen.add(freq)

done = False
while True:
    for line in data:
        op = line[0]
        num = int(line[1:])
        if op == '+':
            freq += num
        elif op == '-':
            freq -= num
        else:
            print('wtf, op=',op)
        if freq in seen:
            print(freq)
            done = True
            break ;
        else:
            seen.add(freq)
    if done:
        break
