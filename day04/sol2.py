#!/usr/bin/env python3

#
#advent of code 2018
#day 04
#part 2
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
        i += 1
        while True and i < len(data):
            if event_type(data[i]) == 'a' and event_type(data[i+1]) == 'u':
                falls = minutes(data[i])
                wakes = minutes(data[i+1])
                while falls < wakes:
                    if falls not in d:
                        d[falls] = {}
                    if g not in d[falls]:
                        d[falls][g] = 0
                    d[falls][g] += 1
                    falls += 1
            elif event_type(data[i]) == '#':
                break
            else:
                print('wtf, line=', i)
                break
            i += 2
            
  
#we have an array of minutes 0..59
#each minute has an array of guards


res_guard = None
res_minute = None
res_time = 0
for k,v in d.items():   #k = minute
    for guard, amount in v.items():
        if amount > res_time:
            res_guard = guard
            res_minute = k
            res_time = amount

print(res_guard * res_minute)

