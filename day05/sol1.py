#!//nfs/2016/a/asarandi/.brew/Frameworks/Python.framework/Versions/3.7/bin/python3.7

#
#advent of code 2018
#day 05
#part 1, unoptimized
#

with open('input.txt') as fp:
    data = fp.read().splitlines()[0]
    fp.close()

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

with open('input2.txt', 'w') as fp:
    fp.write(data)
    fp.close()

print(len(data))
