#!/usr/bin/env python3

#
#advent of code 2018
#day 14
#part 1
#

def print_data(data):
    for j in range(len(data)):
        if j == idx_first:
            print('(%d)' % (data[j]), end='')
        elif j == idx_second:
            print('[%d]' % (data[j]), end='')
        else:
            print(' %d ' % (data[j]), end='')
    print()

data = [3, 7]
idx_first = 0
idx_second = 1

i = 0
res = []
puzzle = 652601
done = False
while not done:
    added = list(str(data[idx_first] + data[idx_second]))
    for digit in added:
        data.append(int(digit))
        if len(data) > puzzle:
            res.append(int(digit))
        if len(res) >= 10:
            done = True
            break

    idx_first = int((data[idx_first] + 1 + idx_first) % len(data))
    idx_second = int((data[idx_second] + 1 + idx_second) % len(data))

    i += 1

for digit in res:
    print(digit, end='')
print()
