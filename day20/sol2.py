#!/usr/bin/env python3

import os
import sys
import time

#
#advent of code 2018
#day 20
#part 2
#


DEFAULT_SYM = '#'

def add_left_column(data):
    for row in data:
        row.insert(0, DEFAULT_SYM)

def add_right_column(data):
    for row in data:
        row.append(DEFAULT_SYM)

def add_top_row(data):
    newrow = [DEFAULT_SYM for x in range(len(data[0]))]
    data.insert(0, newrow)

def add_bottom_row(data):
    newrow = [DEFAULT_SYM for x in range(len(data[0]))]
    data.append(newrow)

def border_frame(data):
    add_left_column(data)
    add_right_column(data)
    add_top_row(data)
    add_bottom_row(data)

def go_west(data,y,x):
    x -= 1
    if x < 0:
        add_left_column(data)
        x = 0

    if data[y][x] != 'X':    
        data[y][x] = '|'
    x -= 1
    if x < 0:
        add_left_column(data)
        x = 0
    if data[y][x] != 'X':    
        data[y][x] = '.'
    return (y,x)

def go_east(data,y,x):
    x += 1
    if x >= len(data[y]):
        add_right_column(data)
        x = len(data[y]) - 1
        
    if data[y][x] != 'X':    
        data[y][x] = '|'
    x += 1
    if x >= len(data[y]):
        add_right_column(data)
        x = len(data[y]) - 1

    if data[y][x] != 'X':    
        data[y][x] = '.'
    return (y,x)

def go_north(data,y,x):
    y -= 1
    if y < 0:
        add_top_row(data)
        y = 0

    if data[y][x] != 'X':    
        data[y][x] = '-'
    y -= 1
    if y < 0:
        add_top_row(data)
        y = 0

    if data[y][x] != 'X':    
        data[y][x] = '.'
    return (y,x)

def go_south(data,y,x):
    y += 1
    if y >= len(data):
        add_bottom_row(data)
        y = len(data) - 1

    if data[y][x] != 'X':    
        data[y][x] = '-'
    y += 1
    if y >= len(data):
        add_bottom_row(data)
        y = len(data) - 1

    if data[y][x] != 'X':    
        data[y][x] = '.'
    return (y,x)


def get_doors(data,y,x):
    res = []
    if data[y][x+1] == '|':
        res.append((y,x+2))
    if data[y][x-1] == '|':
        res.append((y,x-2))
    if data[y+1][x] == '-':
        res.append((y+2,x))
    if data[y-1][x] == '-':
        res.append((y-2,x))
    return res

def print_game(data):
    os.system('clear')
    for line in data:
        print(''.join(line))


def bfs(data,origin,destination):
#    print('origin',origin,'destination',destination)
    queue = [origin]
    clist = [0]
    visited = {origin:1}
    while len(queue) > 0:
        y,x = queue.pop(0)
        count = clist.pop(0)
        count += 1
#        print(y,x)
        doors = get_doors(data,y,x)
        for door in doors:
#            print('count',count)
            if door == destination:
                return (count)
            if door not in visited:
                queue.append(door)
                clist.append(count)
                visited[door] = (y,x)
    return -1
                
#    print('result:', csave-1)


if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = 'sample.txt'
with open(fn) as fp:
    game = fp.read().splitlines()[0]
    fp.close()

game = list(game)

data = [['#' for x in range(500)] for y in range(500)]

stack = []
i = 0
x = 250
y = 250
data[y][x] = 'X'
while True:
    if i < len(game):
        sym = game[i]
        if sym == 'W':
            y,x = go_west(data,y,x)            
        elif sym == 'E':
            y,x = go_east(data,y,x)
        elif sym == 'N':
            y,x = go_north(data,y,x)
        elif sym == 'S':
            y,x = go_south(data,y,x)
        elif sym == '(':
            stack.append((y,x))
        elif sym == '|':

#            print('split',y,x)
            y, x = stack[-1]
#            print('split',y,x)
        elif sym == ')':
            #y, x = 
            stack.pop()
        elif sym == '^':
            pass
        elif sym == '$':
            pass

#        print(i, sym)
#        for row in data:
#            print(''.join(row))
#        print()


    else:
        break
    i += 1

#border_frame(data)
#for row in data:
#    print(''.join(row))
#print()


done = False
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'X':
            done = True
            break
    if done:
        break

origin = (y,x)
res = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == '.':
            cnt = bfs(data,origin,(y,x))
            if cnt >= 1000:
                res += 1

print(res)
