#!/usr/bin/env python3

from collections import deque

#
#advent of code 2018
#day 15
#part 1
#



#
# rounds +=1
# for u in units:
#     unit_take_turn(u, ldata)
#
#


def unit_take_turn(unit, ldata):
# if_enemy_in_range:Z
#     attackZ
# else:
#     move
    pass


#identify all possible targets
# if no targets,
#   combat ends

# identify open squares in range of each target
# if not already in range,
# and no adjacent open squares next to any target
# then unit ends turn

# if in range of target, contine with attack
#


#To move, the unit first considers the squares that are in range and determines which of those squares it could reach in the fewest steps.
#A step is a single movement to any adjacent (immediately up, down, left, or right) open (.) square.
#If multiple squares are in range and tied for being reachable in the fewest steps, the step which is first in reading order is chosen.


# if new_found path is shorter than the paths in found paths list,
# then destroy the paths list and create a new one with the shortest path
# add more paths to list if same length,
# and if shorter, then destroy existing list of possible paths and create a new one w/ shortest path 
# if multiple shortest paths exist, choose one in reading order: top->bottom, left->right

#------------------------------------------------------------------------------
def mark_in_range(unit, ldata):
    enemy_dict = {'E':'G', 'G':'E'}
    res = []
    for x in range(len(ldata)):
        for y in range(len(ldata[x])):
            char = ldata[x][y]
            if char == enemy_dict[unit]:
                if x > 0             and ldata[x-1][y] == '.':
                    ldata[x-1][y] = '?'
                    res.append([x-1,y])
                if x < len(ldata)    and ldata[x+1][y] == '.':
                    ldata[x+1][y] = '?'
                    res.append([x+1,y])
                if y > 0             and ldata[x][y-1] == '.':
                    ldata[x][y-1] = '?'
                    res.append([x,y-1])
                if y < len(ldata[x]) and ldata[x][y+1] == '.':
                    ldata[x][y+1] = '?'
                    res.append([x,y+1])
    return res

#------------------------------------------------------------------------------
def clear_in_range(ldata):
    for x in range(len(ldata)):
        for y in range(len(ldata[x])):
            if ldata[x][y] == '?': ldata[x][y] = '.'


class Node:
    def __init__ (self, ldata, x, y, walkable):
        self.x = x
        self.y = y
        self.visited = False
        self.parent = None
        self.walkable = walkable

        self.up = None
        self.right = None
        self.down = None
        self.left = None

        row_len = len(ldata[x])
        col_height = len(ldata)

        if x > 0            :self.up = (x-1) * row_len + y
        if x < col_height   :self.down = (x+1) * row_len + y
        if y > 0            :self.left = x * row_len + y - 1
        if y < row_len      :self.right = x * row_len + y + 1



#------------------------------------------------------------------------------
def get_adjacent_unvisited(current, board, ldata):
    x = current.x
    y = current.y
    if board[current.up].visited == False:  return board[current.up]
    if board[current.down].visited == False:  return board[current.down]
    if board[current.left].visited == False:  return board[current.left]
    if board[current.right].visited == False:  return board[current.right]
    return None


def reverse_path(current, start):
    res = []
    while True:
        x = current.x
        y = current.y
        if [x,y] == start:  # do not append actual start position
            break           #
        res.append([x,y])   #
        current = current.parent
    return res[::-1]        #reverse order

def is_reachable(ldata, start, end):
    board = {}
    for x in range(len(ldata)):
        for y in range(len(ldata[x])):
            walkable = False
            if ldata[x][y] == '.':
                walkable = True
            board[x*len(ldata[x])+y] = Node(ldata, x, y, walkable)
    x, y = start
    root = board[x*len(ldata)+y]
    root.walkable = True
    root.visited = True
    queue = deque([root])
    res = []
    while len(queue) > 0:
        current = queue.popleft()
        if [current.x, current.y] == end:
            res.append(reverse_path(current, start))
        while True:
            adj = get_adjacent_unvisited(current, board, ldata)
            if not adj:
                break
            adj.visited = True
            if not adj.walkable:
                continue
            adj.parent = current
            queue.append(adj)
    return res

#------------------------------------------------------------------------------
def list_all_units(ldata):  #ldata = list of lists
    valid_unit_types = ['E', 'G']
    res = []
    for x in range(len(ldata)):
        row = ldata[x]
        for y in range(len(row)):
            char = ldata[x][y]
            if char in valid_unit_types:
                res.append([char, x, y, 3, 200])    #unit, row, col, attack, hp
    return res

def is_end_of_game(units):
    elves = 0
    goblins = 0
    for u in units:
        if u[0] == 'E':
            elves += 1
        else:
            goblins += 1
    if not elves or not goblins:
        return True
    return False


with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()
ldata = []
for line in data:
    ldata.append(list(line))
    print(list(line))

units = list_all_units(ldata)
#print(units)

print(is_reachable(ldata,[3,11],[3,5]))
