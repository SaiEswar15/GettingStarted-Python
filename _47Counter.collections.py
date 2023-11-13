'''what is the use case of counter'''

#answer : when we have list of elements and we want to have the frequency of all the elements 
#this is the usecase for the usecase for using counter


myList = list()

print(myList, type(myList))  #empty list

myList = ['a', 'b', 'c', 'a', 'c', 'd', 'd', 'b', 'a']

#now we want the frequency of all elements 
myDict = dict()

#soultion : using the dictionary
for el in myList :
    if el in myDict :
        myDict[el] += 1
    else :
        myDict[el] = 1

print(myDict)

'''this can be simplified using the counter from the collections'''

from collections import Counter 

result = Counter(myList)

print(result, 'using counter collections')

#if we want the clean dictionary 
print(dict(result), 'using counter collections')

#if you want the detailed view 
#solution : we can use elements 
print(list(result.elements()), 'detailed view') 
#detailed view will be available in list 

'''we already know that if we have dict we can use the keys and values and items'''
#keys, values and items will be available in list 

print(list(result.keys()), 'print keys')
print(list(result.values()), 'print values')
print(list(result.items()), 'print items')





