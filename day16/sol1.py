#!/usr/bin/env python3

import copy

#
#advent of code 2018
#day 16
#part 1
#

def addr(reg,a,b,c):
    reg[c] = reg[a] + reg[b]

def addi(reg,a,b,c):
    reg[c] = reg[a] + b

def mulr(reg,a,b,c):
    reg[c] = reg[a] * reg[b]

def muli(reg,a,b,c):
    reg[c] = reg[a] * b

def banr(reg,a,b,c):
    reg[c] = reg[a] & reg[b]

def bani(reg,a,b,c):
    reg[c] = reg[a] & b

def borr(reg,a,b,c):
    reg[c] = reg[a] | reg[b]

def bori(reg,a,b,c):
    reg[c] = reg[a] | b

def setr(reg,a,b,c):
    reg[c] = reg[a]

def seti(reg,a,b,c):
    reg[c] = a

def gtir(reg,a,b,c):
    if a > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0

def gtri(reg,a,b,c):
    if reg[a] > b:
        reg[c] = 1
    else:
        reg[c] = 0

def gtrr(reg,a,b,c):
    if reg[a] > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0

def eqir(reg,a,b,c):
    if a == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0

def eqri(reg,a,b,c):
    if reg[a] == b:
        reg[c] = 1
    else:
        reg[c] = 0

def eqrr(reg,a,b,c):
    if reg[a] == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

samples = []
i = 0
while i < len(data):
    if data[i][0:5] == 'Befor' and data[i+2][0:5] == 'After':
        before = [int(k) for k in data[i][9:-1].split(',')]
        opcode = [int(k) for k in data[i+1].split(' ')]
        after  = [int(k) for k in data[i+2][9:-1].split(',')]
        samples.append([before,opcode,after])
        i += 4
    else:
        break

instructions = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

count = 0
for s in samples:
    before = s[0]
    opcode = s[1]
    after  = s[2]
    matches = 0
    for instr in instructions:
        reg = copy.deepcopy(before)
        instr(reg, opcode[1], opcode[2], opcode[3])
        if reg == after:
            matches += 1

    if matches >= 3:
        count += 1

print('result:',count)
        
