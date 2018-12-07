#!/usr/bin/env python3

#
#advent of code 2018
#day 07
#part 1
#

def all_finished(steps):
    for step in steps:
        if not steps[step]['finished']:
            return False
    return True

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

steps = {}
for line in data:
    req = line[5:6]
    name = line[36:37]
    if req not in steps:
        steps[req] = {}
        steps[req]['req'] = []
    if name not in steps:
        steps[name] = {}
        steps[name]['req'] = []
    steps[name]['req'].append(req)

for step in steps:
    steps[step]['finished'] = False

output = ''
while not all_finished(steps):
    for k in sorted(steps):
        if len(steps[k]['req']) == 0 and not steps[k]['finished']:
            steps[k]['finished'] = True
            output += k
            for s in steps:
                if k in steps[s]['req']:
                    steps[s]['req'].remove(k)
            break
print(output)
