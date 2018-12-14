#!/usr/bin/env python3

#
#advent of code 2018
#day 13
#part 2
#

def is_cart(character):
    shapes = ['^', 'v', '<', '>']
    if character in shapes:
        return True
    return False

def cart_turn_left(c):
    if c == '^': return '<'
    if c == '>': return '^'
    if c == 'v': return '>'
    if c == '<': return 'v'

def cart_turn_right(c):
    if c == '^': return '>'
    if c == '>': return 'v'
    if c == 'v': return '<'
    if c == '<': return '^'

def cart_intersection_turn(c):
    if c[1] % 3 == 0:
        c[0] = cart_turn_left(c[0])
    elif c[1] % 3 == 1:
        pass
    elif c[1] % 3 == 2:
        c[0] = cart_turn_right(c[0])
    c[1] += 1

def cart_curve_turn(c, t):
    if t == '/':
        if c[0] == 'v' or c[0] == '^':
            c[0] = cart_turn_right(c[0])
        else:
            c[0] = cart_turn_left(c[0])
    elif t == '\\':
        if c[0] == '>' or c[0] == '<':       
            c[0] = cart_turn_right(c[0])
        else:
            c[0] = cart_turn_left(c[0])

def cart_move(c):   #return updated coords
    if c[0] == '^':
        c[2] -= 1
    if c[0] == '>':
        c[3] += 1
    if c[0] == 'v':
        c[2] += 1
    if c[0] == '<':
        c[3] -= 1
    return c[2], c[3]

def is_collision(carts):
    for a in carts:
        if carts[a][4] == 0:
            for b in carts:
                if carts[b][4] == 0:
                    if a != b and carts[a][2] == carts[b][2] and carts[a][3] == carts[b][3]:
                        return True
    return False

def print_game(carts,data):
    save = []
    for c in carts:
        i = carts[c][2]
        j = carts[c][3]
        save.append([data[i][j], i, j])
        data[i][j] = carts[c][0]
    for line in data:
        print(''.join(line))
    for s in save:
        i = s[1]
        j = s[2]
        data[i][j] = s[0]

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

ldata = []
for line in data:
    ldata.append(list(line))

data = ldata

carts = {}
k = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        character = data[i][j]
        if is_cart(character):
            carts[k] = [character,0,i,j,0]      # zero for turn index
            k += 1
            new_character = '|'
            if character == '>' or character == '<':
                new_character = '-'
            data[i][j] = new_character



def count_active(carts):
    res = 0
    for c in carts:
        if carts[c][4] == 0:
            res += 1
    return res

#
# look into sort with lambda key
#

def bubble_sort_carts_by_value_index(carts, k):
    done = False
    while not done:
        done = True
        i = 1
        while i < len(carts):
            if carts[i][k] < carts[i-1][k]:
                tmp = carts[i]
                carts[i] = carts[i-1]
                carts[i-1] = tmp
                done = False
                continue
            i += 1
    return carts

while count_active(carts) > 1:
    carts = bubble_sort_carts_by_value_index(carts, 3)
    carts = bubble_sort_carts_by_value_index(carts, 2)
    for c in carts:
        if carts[c][4] == 0:
            i, j = cart_move(carts[c])
            sym = data[i][j]
            if sym == '+':
                cart_intersection_turn(carts[c])
            if sym == '\\' or sym == '/':
                cart_curve_turn(carts[c], sym)
            if is_collision(carts):
                for x in carts:
                    if carts[x][4] == 0 and carts[x][2] == i and carts[x][3] == j:
                        carts[x][2] = -1
                        carts[x][3] = -1
                        carts[x][4] = -1
#                print('collision:',j,i)

for c in carts:
    if carts[c][4] == 0:
        print("%d,%d" % (carts[c][3], carts[c][2]))
#        print('active:',carts[c])


