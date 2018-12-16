#!/usr/bin/env python3

import os
import sys
import time
from collections import deque
from operator import itemgetter

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
def get_end_positions(unit, ldata):
    enemy_dict = {'E':'G', 'G':'E'}
    res = []
    for x in range(len(ldata)):
        for y in range(len(ldata[x])):
            char = ldata[x][y]
            if char == enemy_dict[unit[0]]:
                if x > 0             and ldata[x-1][y] == '.':
                    res.append([x-1,y])
                if x < len(ldata)    and ldata[x+1][y] == '.':
                    res.append([x+1,y])
                if y > 0             and ldata[x][y-1] == '.':
                    res.append([x,y-1])
                if y < len(ldata[x]) and ldata[x][y+1] == '.':
                    res.append([x,y+1])
    return res

#------------------------------------------------------------------------------

node_max_score = 999999999

class Node:
    def __init__ (self, ldata, x, y, end):
        self.x = x
        self.y = y
        self.visited = False
        self.parent = None

        self.walkable = False
        if ldata[x][y] == '.':
            self.walkable = True

        self.f = node_max_score
        self.g = node_max_score
        self.h = abs(end[0] - x) + abs(end[1] - y)

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

def get_adjacent_nodes(current, board):
    if board[current.right].visited == False:  return board[current.right]
    if board[current.left].visited == False:  return board[current.left]
    if board[current.down].visited == False:  return board[current.down]
    if board[current.up].visited == False:  return board[current.up]
    return None

def reverse_path(current, start):
    res = []
    while True:
        x = current.x
        y = current.y
        res.append([x,y])
        if [x,y] == start:
            break
        current = current.parent
    return res[::-1]        #reverse order


def get_lowest_f_score(openset):
    res_idx = -1
    res_score = node_max_score
    for node in openset:
        if node.f < res_score:
            res_score = node.f
            res_idx = openset.index(node)
    return openset.pop(res_idx)


def is_reachable(ldata, start, end):
    board = {}
    for x in range(len(ldata)):
        for y in range(len(ldata[x])):
            id_ = x * len(ldata[x]) + y
            board[id_] = Node(ldata, x, y, end)
    x, y = start
    root = board[x*len(ldata[x])+y]
    root.walkable = True
    root.visited = True
    root.g = 0
    openset = [root]
    res = []
    while len(openset) > 0:
        current = get_lowest_f_score(openset)   #get item with lowest f score
        if [current.x, current.y] == end:
            return reverse_path(current, start)
        while True:
            adj = get_adjacent_nodes(current, board)
            if not adj: break
            adj.visited = True
            if not adj.walkable: continue
            tentative_g = current.g + 1 #distance from current          
            if adj not in openset:
                openset.append(adj)
            if tentative_g >= adj.g:
                continue
            adj.parent = current
            adj.g = tentative_g
            adj.f = adj.g + adj.h
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
        if u[0] == 'E' and u[4] > 0:
            elves += 1
        elif u[0] == 'G' and u[4] > 0:
            goblins += 1
    if not elves or not goblins:
        return True
    return False

def get_start_positions(unit, ldata):
    x = unit[1]
    y = unit[2]
    res = []
    if x > 0:
        if ldata[x-1][y] == '.':
            res.append([x-1,y])
    if y > 0:
        if ldata[x][y-1] == '.':
            res.append([x,y-1])
    if y < len(ldata[x]):
        if ldata[x][y+1] == '.':
            res.append([x,y+1])
    if x < len(ldata):
        if ldata[x+1][y] == '.':
            res.append([x+1,y])
    return res

fn='sample2.txt'
if len(sys.argv) > 1:
    fn = sys.argv[1]
with open(fn) as fp:
    data = fp.read().splitlines()
    fp.close()
ldata = []
for line in data:
    ldata.append(list(line))

units = list_all_units(ldata)

def get_shortest_path_len(paths):
    if len(paths) < 1:
        return 0
    min_len = node_max_score
    for p in paths:
        if len(p) < min_len and len(p) > 0:
            min_len = len(p)
    return min_len

def remove_longer_paths(paths, min_len):
    done = False
    while not done:
        done = True
        for i in range(len(paths)):
            if len(paths[i]) > min_len:
                paths.pop(i)
                done = False
                break
    return paths



def get_unit_by_coords(x,y,units):
    for u in units:
        if u[1] == x and u[2] == y:
            return u
    return None


def is_attack(unit, units, ldata):             
    enemy_dict = {'E':'G', 'G':'E'}
    enemy = enemy_dict[unit[0]]
    x = unit[1]
    y = unit[2]
    res = []
    if y < len(ldata[x]):               #right
        if ldata[x][y+1] == enemy:
            res.append(get_unit_by_coords(x,y+1,units))

    if x < len(ldata):                  #down
        if ldata[x+1][y] == enemy:
            res.append(get_unit_by_coords(x+1,y,units))

    if y > 0:                           #left
        if ldata[x][y-1] == enemy:
            res.append(get_unit_by_coords(x,y-1,units))
    if x > 0:                           #up
        if ldata[x-1][y] == enemy:
            res.append(get_unit_by_coords(x-1,y,units))

    if len(res) > 0:
        res = sorted(res, key=itemgetter(4))    #sort by hp
        res = [u for u in res if u[4] > 0]
        lhp = res[0][4]
        res = [u for u in res if u[4] <= lhp]
        res = sorted(res, key=itemgetter(2))    #sort by y coord
        res = sorted(res, key=itemgetter(1))    #sort by x coord

    else:
        res = None
    return res


def print_game(ldata, units):
#    os.system('clear')
    for row in ldata:
        print(row)
    for u in units:
        print(u)
#    time.sleep(0.1)


def sort_units(units):
    i = len(units) - 1
    while i >= 0:
        if units[i][4] < 0:
            units.pop(i)
        i -= 1


    sort1 = sorted(units, key=itemgetter(2))
    res = sorted(sort1, key=itemgetter(1))
    return res


def count_units(ldata, sym):
    res = 0
    for x in ldata:
        for y in x:
            if y == sym:
                res += 1
    return res



done = False
rounds = 0
full_rounds = 0
goblins = 0
elvles = 0
while not done:
    units = sort_units(units)
    for u in units:
        goblins = count_units(ldata, 'G')
        elves = count_units(ldata, 'E')
        if is_end_of_game(units):
            done = True
            print('game over, break')
            rounds -= 1
            break
        else:
            print('round #', rounds)
            print_game(ldata, units)
            print()


        if u[4] > 0:
            enemies = is_attack(u, units, ldata)
            if enemies:
                print('enemies 1', enemies)
                enemy = enemies[0]  #should be sorted by hp                  
                enemy[4] -= u[3]                #enemy hp -= unit attack
                if enemy[4] <= 0:   #dead?                            
                    ldata[enemy[1]][enemy[2]] = '.'
                    if enemy[0] == 'E': elves -= 1
                    if enemy[0] == 'G': goblins -= 1
                    if elves == 0 or goblins == 0:
                        print('break #1')
                        done = True
                        
            else:
                end = get_end_positions(u, ldata)
                if len(end) == 0:
                    continue
                start = get_start_positions(u, ldata)
                paths = []
                for src in start:
                    for dst in end:
                        p = is_reachable(ldata, src, dst)
                        if len(p) > 0:
                            paths.append(p)

                if len(paths) > 0:
                    min_len = get_shortest_path_len(paths)
                    paths = sorted(remove_longer_paths(paths, min_len))
                    print(paths)
                    x, y = paths[0][0]
                    ldata[u[1]][u[2]] = '.'
                    ldata[x][y] = u[0]
                    u[1] = x
                    u[2] = y
                    
                    enemies = is_attack(u, units, ldata)
                    if enemies:
                        print('enemies 2', enemies)
                        enemy = enemies[0]  #should be sorted by hp                  
                        enemy[4] -= u[3]                #enemy hp -= unit attack
                        if enemy[4] <= 0:   #dead?                            
                            ldata[enemy[1]][enemy[2]] = '.'
                            if enemy[0] == 'E': elves -= 1
                            if enemy[0] == 'G': goblins -= 1
                            if elves == 0 or goblins == 0:
                                print('break #2')
                                done = True
                                                                        
    rounds += 1



full_rounds = rounds
sum_hp = 0
for u in units:
    if u[4] > 0:
        sum_hp += u[4]


units = sort_units(units)
print_game(ldata, units)
print('full rounds',full_rounds, 'sum_hp', sum_hp)
print('units',units)
print('result:', sum_hp * full_rounds)

