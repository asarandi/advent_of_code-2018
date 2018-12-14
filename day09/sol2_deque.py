#!/usr/bin/env python3

from collections import deque

#
#advent of code 2018
#day 09
#part 2 version 3 w/ deque
#

num_marbles = 71944 * 100
num_players = 423

#----------------------------------------------------------

players = {}
for p in range(0, num_players):
    players[p] = 0

current = deque([0])

res = 0    #result
i = 1
while i < num_marbles + 1:
    if i % 23 == 0:
        idx = (i - 1) % num_players
        players[idx] += i
        current.rotate(7)
        players[idx] += current.pop()
        current.rotate(-1)
        if players[idx] > res:
            res = players[idx]
    else:
        current.rotate(-1)
        current.append(i)
    i += 1

print(res)
