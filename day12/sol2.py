#!/usr/bin/env python3

#
#advent of code 2018
#day 12
#part 2
#

left_padding = 100
stable_gen = 400
right_padding = stable_gen + 100

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

state = left_padding * '.' + data[0][15:] + '.' * right_padding

keys = []
values = []
for line in data[2:]:
    keys.append(line[:5])
    values.append(line[9:])

def make_nextgen(state):
    nextgen = list('.' * len(state))
    i = 0
    while i < len(state) - 5:
        sub = state[i:i+5]
        if sub in keys:
            idx = keys.index(sub)
            nextgen[i+2] = values[idx]
        i += 1
    return (''.join(nextgen))


original = state
for i in range(stable_gen):
    state = make_nextgen(state)

stripped = state.strip('.')
diff = state.index(stripped) - stable_gen

res = 0
j = 0
while j < len(stripped):
    if stripped[j] == '#':
        res += j + 50000000000 + diff - left_padding
    j += 1
print(res)
