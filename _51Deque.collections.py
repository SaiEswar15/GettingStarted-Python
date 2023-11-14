# python _51Deque.collections.py

'''deque is used instead of list'''

'''while already we have the list why does we need deque 
there must be some problem with list'''

'''problem : can we insert elements at the end of the list --yes
can we insert elements at the start odf the list --no
can we extend list at the end of the existing list --no
can we extend list at the start of the existing list --yes'''

'''try'''

myList = list()

print(myList)

myList.append(12)
myList.append(13)
myList.append(14)
myList.append(15)

print(myList)

myList.pop()

print(myList)

myList.remove(12)

print(myList)

myList.extend([21,22])

print(myList)

'''so to inset and extend from the front use deque'''

from collections import deque

myList2 = deque([1,4,5,6])

print(myList2, 'deque list')

myList2.appendleft(0)

print(myList2, 'left apppend')

myList2.append(0)

print(myList2, 'right apppend')

myList2.popleft()

print(myList2, 'left pop')

myList2.pop()

print(myList2, 'right pop')


myList2.extendleft([21,22])

print(myList2, 'extend left')

myList2.extend([21,22])

print(myList2, 'extend right')

'''we can rotate the list by 1 step 2 steps etc clockwise and anti'''

myList2.rotate(1)

print(myList2, 'rotated one step')

myList2.rotate(2)

print(myList2, 'rotated two step')
