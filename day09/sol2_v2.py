#!/usr/bin/env python3

#
#advent of code 2018
#day 09
#part 2 version 2
#

#
# here is a solution with a doubly linked list
# input: marbles=7194400, players=423, solving time=27 seconds  .. still slow
#
#e1z4r6p21% time ./sol2_v2.py
#3505711612
#./sol2_v2.py  25.91s user 0.60s system 99% cpu 26.725 total
#


# node class template
# http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data
    def setData(self,newdata):
        self.data = newdata

    def getNext(self):
        return self.next
    def setNext(self,newnext):
        self.next = newnext

    def getPrev(self):
        return self.prev
    def setPrev(self,newprev):
        self.prev = newprev


num_marbles = 7194400
num_players = 423

#----------------------------------------------------------

players = {}
for p in range(0, num_players):
    players[p] = 0

current = Node(0)
current.setNext(current)
current.setPrev(current)

res = 0    #result
i = 1
while i < num_marbles + 1:
    if i % 23 == 0:
        idx = (i - 1) % num_players
        players[idx] += i
        for _ in range(7):
            current = current.getPrev()
        players[idx] += current.getData()

        if players[idx] > res:   # save max
            res = players[idx]

        prev0 = current.getPrev()   #remove current node and fix pointers
        next0 = current.getNext()
        prev0.setNext(next0)
        next0.setPrev(prev0)
        del current
        current = next0

    else:                           #insert a new node
        next1 = current.getNext()
        next2 = current.getNext().getNext()
        newnode = Node(i)
        newnode.setPrev(next1)
        newnode.setNext(next2)
        next1.setNext(newnode)
        next2.setPrev(newnode)
        current = newnode
    i += 1

print(res)
