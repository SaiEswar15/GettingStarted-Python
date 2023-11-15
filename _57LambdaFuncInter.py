# python _57LambdaFuncInter.py

sample = lambda x,y : x+y

print(sample(2,3))

'''why is lambda functions used?'''

#solution : when is only single line of code to execute 
#we can make use of the lambda functions 

'''Places where we use lambda functions ?'''

#solution : we can use them in 
#sorting functions
#map, filter and reduce functions more frequently 

'''example :'''

#this is a simple sort function
myList = [1,2,3,4,5,0,2,5,12,]
myList2 = sorted(myList, reverse = True)
print(myList, myList2)

#lets consider the complex sorting function
tupleList = [(1,3),(2,4),(9,5),(3,5)]
print(sorted(tupleList))

'''now consider sorting using the y index'''

#sure we should apply some functionality

def sortByY(el):
    return el[1]
print(sorted(tupleList, key=sortByY), "sort by 2nd point")

#instead of using the function try using lambda function and also reverse

print(sorted(tupleList, key = lambda x : x[1], reverse = True),"lamda")


"""now sort according to the total sum of each tuple"""

print(sorted(tupleList, key = lambda x : x[0]+x[1]), "sum sorted")


'''we can use lamda functions in map functions'''

arr = [1,2,3,4,5,6]

result = map(lambda el : el+el, arr)
print(list(result) , "map result")


filterResult = filter(lambda el : el<3, arr)
print(list(filterResult), "filter result")

from functools import reduce

reduceResult = reduce(lambda total, el : total+el, arr)
print(reduceResult, "reduce result ")