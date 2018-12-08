#!/usr/bin/env python3

#
#advent of code 2018
#day 08
#part 2
#

def recurse(nodes):
    children = nodes[0]
    num_meta = nodes[1]
    if children == 0:
        j = 0
        c_res = 0
        while j < num_meta:
            c_res += nodes[j + 2]
            j += 1
        return(j + 2, c_res)

    else:
        i = 0
        dist = 0
        values = []
        while i < children:
            d, val = recurse(nodes[dist + 2:])
            dist += d
            values.append(val)
            i += 1
        k = 0
        p_res = 0
        while k < num_meta:
            idx = nodes[k + dist + 2]
            if idx - 1 < len(values):
                p_res += values[idx - 1]
            k += 1
        return (k + dist + 2, p_res)

#------------------------------------------------

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

nodes = []
for n in data[0].split(' '):
    nodes.append(int(n))

dist, res = recurse(nodes)
print(res)
