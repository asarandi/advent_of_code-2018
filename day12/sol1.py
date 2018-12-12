#!/usr/bin/env python3

#
#advent of code 2018
#day 12
#part 1
#

left_padding = 100
right_padding = 100

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

initial = left_padding * '.' + data[0][15:] + '.' * right_padding

keys = []
values = []
for line in data[2:]:
    keys.append(line[:5])
    values.append(line[9:])

def make_nextgen(initial):
    nextgen = list('.' * len(initial))
    i = 0
    while i < len(initial) - 5:
        sub = initial[i:i+5]
        if sub in keys:
            idx = keys.index(sub)
            nextgen[i+2] = values[idx]
        i += 1
    return (''.join(nextgen))

for i in range(20):
    initial = make_nextgen(initial)

data = list(initial)
res = 0
j = 0
while j < len(data):
    if data[j] == '#':
        res += j - left_padding
    j += 1
print(res) 
