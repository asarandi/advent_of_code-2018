#!/usr/bin/env python3

import  sys
import  copy
import  time

#
#advent of code 2018
#day 21
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



fn = 'input.txt'
if len(sys.argv) > 1:
    fn = sys.argv[1]

with open(fn) as fp:
    data = fp.read().splitlines()
    fp.close()

ip = None
prog = []
for line in data:
    if line[0:3] == '#ip':
        ip = int(line.split(' ')[1])
    else:
        sp = line.split(' ')
        instr = sp[0]
        a = int(sp[1])
        b = int(sp[2])
        c = int(sp[3])
        prog.append([instr, a, b, c])

print(prog)


i=0
seen = []
test=5970144
reg = [test,0,0,0,0,0]

while True:


    if i < 0 or i >= len(prog):
        print('success')
        break

    
    instr = prog[i]
    reg[ip] = i
    s = instr[0] + '(reg,int(instr[1]),int(instr[2]),int(instr[3]))'
    before = copy.deepcopy(reg)
    exec(s)
    print(i, instr[0], instr[1], instr[2], instr[3], before, reg)
#    time.sleep(0.05)
    i = reg[ip] + 1


print('result:',reg[0])

