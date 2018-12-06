#!/nfs/2016/a/asarandi/.brew/Frameworks/Python.framework/Versions/3.7/bin/python3.7

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
        j += 1
    i += 1

inf = {}
for k in d:
    inf[k] = False

#print(inf)

edges=[[[0,0], [0,m-1]],        #top
       [[0,0], [m-1,0]],        #left
       [[0,m-1], [m-1,m-1]],    #right
       [[m-1,0],[m-1,m-1]]]     #bottom
    
#print(edges)

for edge in edges:
    x0 = edge[0][0]
    y0 = edge[0][1]
    x1 = edge[1][0]
    y1 = edge[1][1]

    while x0 <= x1:
        y0 = edge[0][1]
        while y0 <= y1:
            c = matrix[x0][y0]
            if c in inf:
                inf[c] = True
            y0 += 1
        x0 += 1


#print(inf)

cnt_max = 0
p_max = None

for p in inf:
    if inf[p] == False:

        cnt = 0
        i = 0
        while i < m:
            j = 0
            while j < m:
                if matrix[i][j] == p:
                    cnt += 1
                j += 1
            i += 1
        if cnt > cnt_max:
            cnt_max = cnt
            p_max = p

#print(p_max, cnt_max)

print(cnt_max)



#for row in matrix:
#    print(''.join(row))

