# python _56infinitetools.itertools.py

from itertools import count, cycle, repeat

#we use these in loops 

for i in range(10) :
    print(i)

for i in count(12) :  #keeps on adding one value until we stop
    print(i)
    if(i==15): 
        break

print('''

''')

myList = [1,2,3]
for i in cycle(myList) :  #keeps on adding one value until we stop
    print(i)
    if i==10 : 
        break



for i in repeat(5) :  #keeps on adding one value until we stop
    print(i)
    if i==10 : 
        break