#!/usr/bin/env python3

#
#advent of code 2018
#day 10
#part 1
#

def get_size(points):
    h_max = 0
    h_min = 0
    v_max = 0
    v_min = 0

    for p in points:
        x = p['pos'][0]
        if x > h_max:
            h_max = x
        if x < h_min:
            h_min = x

        y = p['pos'][1]
        if y > v_max:
            v_max = y
        if y < v_min:
            v_min = y

    return (h_max, h_min, v_max, v_min)

def print_points(points):
    size = get_size(points)

    horizontal = size[0] + abs(size[1])
    vertical = size[2] + abs(size[3])
    matrix = [['.' for x in range(horizontal + 1)] for y in range(vertical + 1)]

    for point in points:
        x = point['pos'][0] + abs(size[1])
        y = point['pos'][1] + abs(size[3])
        matrix[y][x] = '#'
    for row in matrix:
        if '#' in row:
            print(''.join(row))

def age_points(points):
    for p in points:
        p['pos'][0] += p['vel'][0]
        p['pos'][1] += p['vel'][1]

def rewind_points(points):
    for p in points:
        p['pos'][0] -= p['vel'][0]
        p['pos'][1] -= p['vel'][1]

#------------------------------------------------------------------------------

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

points = []
for line in data:
    sp = line.split('> velocity=<')
    pos = sp[0].split('<')[1].strip().split(',')
    vel = sp[1][:-1].strip().split(',')
    points.append( {'pos':[int(pos[0]), int(pos[1])], 'vel':[int(vel[0]), int(vel[1])]} )

while True:
    before = get_size(points)
    age_points(points)
    after = get_size(points)
    if (after >= before):
        break

rewind_points(points)
print_points(points)
