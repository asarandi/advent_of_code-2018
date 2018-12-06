#!/usr/bin/env python3

#
#advent of code 2018
#day 06
#part 1
#

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

d = {}
m = 0

a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
for line in data:
    line = line.split(',')
    x = int(line[0])
    y = int(line[1])
    if x > m: m = x
    if y > m: m = y
    d[a[i]] = [x,y]
    i += 1

m += 1
matrix = [[' ' for x in range(m)] for y in range(m)]

inf = {}
for k in d:
    inf[k] = False

#------------------------------------------------

i = 0
while i < m:
    j = 0
    while j < m:
        dist = m**2
        dupe = False
        p = ' '
        for k,v in d.items():
            cd = abs(i-v[1]) + abs(j-v[0])
            if cd < dist:
                dist = cd
                p = k
                dupe = False
            elif cd == dist:
                dupe = True
        if dupe:
            matrix[i][j] = '.'
        else:           
            matrix[i][j] = p
            if i == 0 or i == m-1:  # edges, inf
                inf[p] = True
            if j == 0 or j == m-1:
                inf[p] = True
        j += 1
    i += 1

#------------------------------------------------

res = 0
for p in inf:
    if inf[p] == False:
        cnt = 0
        for row in matrix:
            cnt += row.count(p)
        if cnt > res:
            res = cnt

print(res)
