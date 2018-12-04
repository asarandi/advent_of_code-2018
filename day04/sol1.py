#!/usr/bin/env python3

#
#advent of code 2018
#day 04
#part 1
#


def event_type(line):
    return line[25:26]

def minutes(line):
    return int(line[15:17])

def guard_id(line):
    return int(line[26:].split(' ')[0])

#----------------------------------------------------------

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

data = sorted(data)
d = {}
i = 0
while i < len(data):
    if event_type(data[i]) == '#':
        g = guard_id(data[i])
        if g not in d:
            d[g] = {}
        i += 1
        while True and i < len(data):
            if event_type(data[i]) == 'a' and event_type(data[i+1]) == 'u':
                falls = minutes(data[i])
                wakes = minutes(data[i+1])
                while falls < wakes:
                    if falls not in d[g]:
                        d[g][falls] = 0
                    d[g][falls] += 1
                    falls += 1
            elif event_type(data[i]) == '#':
                break
            else:
                print('wtf, line=', i)
                break
            i += 2
            

g_id = None
g_slp = 0
for k,v in d.items():
    slp=0
    for m,a in v.items():
        slp += a
    if slp > g_slp:
        g_slp = slp
        g_id = k

g_minute = None
g_amount = 0
for m,a in d[g_id].items():
    if a > g_amount:
        g_minute = m
        g_amount = a

print(g_id * g_minute)
    


