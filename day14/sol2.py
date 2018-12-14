#!/usr/bin/env python3

from collections import deque

#
#advent of code 2018
#day 14
#part 2
#

data = [3, 7]
idx_first = 0
idx_second = 1

puzzle = deque([6,5,2,6,0,1])
last = deque([0,0,0,0,0,0])
while True:
    added = data[idx_first] + data[idx_second]
    if added >= 10:
        data.append(1)
        last.popleft()
        last.append(1)
        if last == puzzle:
            break
    data.append(int(added % 10))
    last.popleft()
    last.append(int(added % 10))
    if last == puzzle:
        break
    idx_first = int((data[idx_first] + 1 + idx_first) % len(data))
    idx_second = int((data[idx_second] + 1 + idx_second) % len(data))

print(len(data) - len(puzzle))

