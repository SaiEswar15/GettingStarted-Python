# python _52products.iterTools.py

#we know that with sets we can do union, intersection, difference, isSubset, issuperset, isDisjoint

#can we do te same with lists
#lets try

'''
myList1 = [1,2]
myList2 = [3]

print(myList1.union(myList2))
'''

#no it is not possible 
#but python gives all the pairs we can form between the two lists
#it uses the product method from itertools

from itertools import product

myList1 = [1,2]
myList2 = [3]
result1 = product(myList1, myList2)
print(list(result1))

#if we want multiple element instead of pairs we can also do by 
result2 = product(myList1, myList2,repeat = 2)
print(list(result2))


