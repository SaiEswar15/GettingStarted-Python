#python _49OrderDict.collections.py

#ordered dictionary is not relevant any more 
#before version 3.7 dict is unordered but now dict is ordered 

#this collection is used to make the dict ordered 

from collections import OrderedDict

myList = OrderedDict({'name' : 'eswar', 'age': 12, 'roll' : 'A2'})

print(dict(myList))
for el in myList :
    print(el, myList[el])

#this is todays general dictionary 

myList2 = {'name' : 'eswar', 'age': 12, 'roll' : 'A2'}
print(myList2)

#both are same