#!/usr/bin/env python3

#
#advent of code 2018
#day 17
#part 1
#

fn='input.txt'
with open(fn) as fp:
    data = fp.read().splitlines()
    fp.close()

all_y = []
all_x = []
for line in data:
    sp = line.split(', ')
    part1=[int(sp[0][2:]), int(sp[0][2:])]
    part2=sp[1][2:].split('..')
    part2=[int(part2[0]), int(part2[1])]
    if sp[0][0] == 'x' and sp[1][0] == 'y':
        part1, part2 = part2, part1
    elif sp[0][0] == 'y' and sp[1][0] == 'x':
        pass
    all_y.append(part1)
    all_x.append(part2)
#    print('y=',part1, 'x=',part2)
    

y_min = 999999999
y_max = -999999999
for y in all_y:
    if min(y) < y_min:  y_min = min(y)
    if max(y) > y_max:  y_max = max(y)

x_min = 999999999
x_max = -999999999
for x in all_x:
    if min(x) < x_min:  x_min = min(x)
    if max(x) > x_max:  x_max = max(x)



matrix = [['.' for x in range(x_max+1)] for y in range(y_max+1)]

for i in range(len(all_y)):
    for y in range(all_y[i][0], all_y[i][1]+1):
        for x in range(all_x[i][0], all_x[i][1]+1):
            matrix[y][x] = '#'


def print_game(matrix):
    for row in matrix:
        print(''.join(row))

def is_end_of_game(matrix, height):
    for x in matrix[height]:
        if x == '~' or x == '|':
            return True
    return False

def is_within_walls(matrix,width,y,x):
    ok_symbols = ['.', '~', '|']
    if matrix[y][x] not in ok_symbols:
        return False
    row = matrix[y]
    to_left = False
    to_right = False
    i = x
    while i < width and row[i] in ok_symbols:
        i += 1
    if i < width and row[i] == '#':
        to_right = True
    i = x
    while i >= 0 and row[i] in ok_symbols:
        i -= 1
    if i >= 0 and row[i] == '#':
        to_left = True
    return to_left and to_right

def is_container_bottom(matrix,height,width,y,x):
    res = False
    ok_symbols = ['.', '~', '|']
    if is_within_walls(matrix,x_max,y,x) and y < height:
        left = x
        while left >= 0 and matrix[y][left] in ok_symbols:
            left -= 1
        right = x
        while right < width and matrix[y][right] in ok_symbols:
            right += 1
        res = True
        for i in range(left+1,right):
            if matrix[y+1][i] != '#':
                res = False
                break
            matrix[y+1][i] = 'z'
    return res

def get_container_walls(matrix,width,y,x):
    ok_symbols = ['.', '~', '|']
    if is_within_walls(matrix,x_max,y,x):
        left = x
        while left >= 0 and matrix[y][left] in ok_symbols:
            left -= 1
        if left < 0 or matrix[y][left] != '#':
            return None
        right = x
        while right < width and matrix[y][right] in ok_symbols:
            right += 1
        if right > width or matrix[y][right] != '#':
            return None
        return left, right
    return None



#matrix[0][500] = '+'
done = False
while not done:
    if is_end_of_game(matrix, y_max):
        done = True
        break
    y = 0
    x = 500
    while y < y_max:
        if is_container_bottom(matrix,y_max,x_max,y,x):
            while is_within_walls(matrix,x_max,y,x):
                left, right = get_container_walls(matrix,x_max,y,x)
                for i in range(left+1,right):
                    matrix[y][i] = '~'
                y -= 1
            done = True
            print('get_walls', get_container_walls(matrix,x_max,y,x))
            break
            # spill left and right




#        print('y,x,walls,bottom',y,x,is_within_walls(matrix,x_max,y,x),is_container_bottom(matrix,y_max,x_max,y,x))
        

        y += 1
    done = True

print_game(matrix)
