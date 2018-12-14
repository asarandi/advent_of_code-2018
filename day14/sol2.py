#!/usr/bin/env python3

#
#advent of code 2018
#day 14
#part 2
#

# slow!! re-implement with sliding window
#e1z4r6p21% time ./sol2.py
#20261485
#./sol2.py  34.89s user 0.16s system 99% cpu 35.120 total
#

data = [3, 7]
idx_first = 0
idx_second = 1

puzzle = [6,5,2,6,0,1]
res = None
while True:
    added = data[idx_first] + data[idx_second]
    if added >= 10:
        data.append(1)
    if data[len(data) - len(puzzle):] == puzzle:
        break
    data.append(int(added % 10))
    if data[len(data) - len(puzzle):] == puzzle:
        break
    idx_first = int((data[idx_first] + 1 + idx_first) % len(data))
    idx_second = int((data[idx_second] + 1 + idx_second) % len(data))

print(len(data) - len(puzzle))

