#!/usr/bin/env python3

#
#advent of code 2018
#day 05
#part 2, slow
#
#e1z4r13p9% time ./sol2.py
#4952
#./sol2.py  9.13s user 0.05s system 99% cpu 9.247 total
#



#----------------------------------------------------------

def react(data):
    more = True
    while more:
        more = False
        i = 0
        while i + 1 < len(data):
            found = False
            two = data[i:i+2].lower()
            if two[0] == two[1]:
                if data[i].isupper() and data[i+1].islower():
                    found = True
                elif data[i].islower() and data[i+1].isupper():
                    found = True
            if found:
                more = True
                data = data[:i] + data[i+2:]
                continue
            i += 1
    return (data)

#----------------------------------------------------------

with open('input2.txt') as fp:
    data = fp.read().splitlines()[0]
    fp.close()

polymers = set(list(data.lower()))

original = data
x_len = len(original)
for polymer in polymers:
    data = [c for c in original if (c != polymer and c != polymer.upper())]
    data = ''.join(data)
    new_len = len(react(data))
    if new_len < x_len:
        x_len = new_len
print(x_len)
