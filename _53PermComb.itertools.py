# python _53PermComb.itertools.py

#for the list we can do permutations and combinations 

from itertools import permutations, combinations, combinations_with_replacement

myList = [1,2,3,4]

p = permutations(myList, 2) #no of elements in each permutation
c = combinations(myList, 2)
cr = combinations_with_replacement(myList, 2)

print(list(p))
print(list(c))
print(list(cr))

#explination about permutations 
#in permuation if we have (1,2) then (2,1) is also considered as permutation
#in combinations we dont consider (2,1) as combination only (1,2) is a combination
#(1,1) can also be combination but only once 

