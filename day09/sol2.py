#!/usr/bin/env python3

#
#advent of code 2018
#day 09
#part 2
#

#
# -- super slow, lots of room for improvement
# https://wiki.python.org/moin/TimeComplexity
# https://www.ics.uci.edu/~brgallar/week8_2.html
#
# maybe implement a deque

#puzzle input
#423 players; last marble is worth 71944 points

#sample input
# 9 players; last marble is worth   25 points: high score is 32
#10 players; last marble is worth 1618 points: high score is 8317
#13 players; last marble is worth 7999 points: high score is 146373
#17 players; last marble is worth 1104 points: high score is 2764
#21 players; last marble is worth 6111 points: high score is 54718
#30 players; last marble is worth 5807 points: high score is 37305

num_marbles = 71944 * 100
num_players = 423

#----------------------------------------------------------

players = {}
for p in range(0, num_players):
    players[p] = 0

board = [0]

i = 0
marble = 1
current = 0
while i < num_marbles:
    if marble % 23 == 0:
        players[i % num_players] += marble
        idx = (current - 7) % len(board)
        players[i % num_players] += board.pop(idx)
        current = idx % len(board)
    else:
        idx = (current + 1) % len(board) + 1
        idx + 1
        current = idx
        board.insert(current, marble)
    marble += 1
    i += 1

amount = 0
for p in players:
    if players[p] > amount:
        amount = players[p]
print(amount)
