#!/usr/bin/env python3

import copy

#
#advent of code 2018
#day 16
#part 2
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

def is_correct_instruction(instr, original, opcode, after):
    before = copy.deepcopy(original)
    instr(before, opcode[1], opcode[2], opcode[3])
    if before == after:
        return True
    return False

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

samples = []
prog = []
i = 0
while i < len(data):
    if data[i][0:5] == 'Befor' and data[i+2][0:5] == 'After':
        before = [int(k) for k in data[i][9:-1].split(',')]
        opcode = [int(k) for k in data[i+1].split(' ')]
        after  = [int(k) for k in data[i+2][9:-1].split(',')]
        samples.append([before,opcode,after])
        i += 4
    else:
        if len(data[i]) > 0:
            prog.append([int(k) for k in data[i].split(' ')])
        i += 1     

instructions = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

samples2 = {}
for i in range(len(instructions)):
    samples2[i] = []
    for s in samples:
        if s[1][0] == i:
            samples2[i].append(samples.pop(samples.index(s)))

identified = {}

while len(instructions) > 0:
    candidates = {}
    for k in samples2:
        candidates[k] = []
        samples = samples2[k]             # array of [ [before] [opcode] [ after] ]
        for instr in instructions:
            wrong = 0
            for s in samples:
                if is_correct_instruction(instr, s[0], s[1], s[2]) == False:
                    wrong += 1
            if wrong == 0:
                candidates[k].append(instr)
    for c in candidates:
        if len(candidates[c]) == 1:
            identified[c] = candidates[c][0]
            instructions.remove(identified[c])

#print(identified)
reg = [0, 0, 0, 0]
for i in prog:
    f = i[0]
    identified[f](reg, i[1], i[2], i[3])

print('result:', reg[0])
