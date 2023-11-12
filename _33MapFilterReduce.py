#map and filter are similar to the js
arr = [1,3,4,9,7]

#map with general function
def normalSolve(el) :
    return el%2==0

generalArray = map(normalSolve, arr)
print(list(generalArray))

#map with lambda function
solve = lambda a : a%2==0

newArray = map(solve, arr)
print(list(newArray))


#filter function 
#filter with normal function
def solveFilterFunction(el):
    return not el%2==0

generalFilterFunction = filter(solveFilterFunction, arr)
print(list(generalFilterFunction))

#filter with lambda function
result = lambda el : not el%2==0

filterArrayLamda = filter(result, arr)
print(list(filterArrayLamda))


#reduce function 
#little different and is not available globally 
#we have to import this 

from functools import reduce

solvingFunction = lambda a,b : a+b

sum = reduce(solvingFunction, arr)
print("reduce", sum)