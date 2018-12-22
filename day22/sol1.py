#!/usr/bin/env python3

#
#advent of code 2018
#day 22
#part 1
#


depth = 4080
target = (785 +1, 14 +1)

game_index = [[0 for x in range(target[1])] for y in range(target[0])]

risk_level = 0
for y in range(target[0]):
    for x in range(target[1]):
        if (y,x) == (0,0):
            geologic_index = 0
        elif y == 0 and x != 0:
            geologic_index = x * 16807
        elif y != 0 and x == 0:
            geologic_index = y * 48271
        else:
            geologic_index = game_index[y-1][x] * game_index[y][x-1]

        erosion_level = (geologic_index + depth) % 20183
        game_index[y][x] = erosion_level
        region_type = erosion_level % 3
        risk_level += region_type

risk_level -= region_type
print(risk_level)

