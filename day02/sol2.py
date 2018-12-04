#!/usr/bin/env python3

#
#advent of code 2018
#day 02
#part 2
#

with open('input.txt') as fp:
    data = fp.read().splitlines()
    fp.close()

done = False
for line1 in data:
    for line2 in data:
        if line1 != line2:
            i = 0
            wrong = 0
            while i < len(line1):
                if line1[i] != line2[i]:
                    wrong += 1
                if wrong > 1:
                    break
                i += 1
            if wrong == 1:
                i = 0
                while i < len(line1):
                    if line1[i] == line2[i]:
                        print(line1[i], end='')
                    i += 1
                print('')
                done = True
                break
        if done:
            break
    if done:
        break
