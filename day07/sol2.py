#!/usr/bin/env python3

#
#advent of code 2018
#day 07
#part 2
#

def available_worker(workers):
    for worker in workers:
        if workers[worker] == None:
            return worker
    return None

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

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for step in steps:
    steps[step]['started'] = False
    steps[step]['finished'] = False
    steps[step]['worker'] = None
    steps[step]['time'] = list(alpha).index(step) + 61


workers = {0:None, 1:None, 2:None, 3:None, 4:None}

sec = 0
while not all_finished(steps):
    for k in sorted(steps):
        if len(steps[k]['req']) == 0:
            if steps[k]['started'] == False:
                w = available_worker(workers)
                if w != None:
                    steps[k]['started'] = True
                    steps[k]['worker'] = w
                    workers[w] = k
    for k in sorted(steps):
        if len(steps[k]['req']) == 0:
            if steps[k]['started'] and not steps[k]['finished']:
                if steps[k]['time'] > 0:
                    steps[k]['time'] -= 1
                if steps[k]['time'] == 0:
                    steps[k]['finished'] = True
                    w = steps[k]['worker']
                    workers[w] = None
                    for s in steps:
                        if k in steps[s]['req']:
                            steps[s]['req'].remove(k)
    sec += 1
print(sec)
