# python _50defaultDict.collections.py

'''if we are using another dict method while already having one 
there must be the problem with the existing one'''

'''the problem is the acessing the item that is not present in the dict'''

'''try acessing the key that is not present in the dict'''

myDict = dict()

myDict = {'name' : 'eswar', 'age' : 12, 'school' : 'pvhs'}

#now acess the key inside the dict

print(myDict['name']) #works

#now try calling the key that is not inside the dict

#print(myDict['gender']) #gives you an error 

'''this might stop the whole appliacation which is not the good practice'''

'''so the default dictionaries come into picture'''

from collections import defaultdict

newDict = defaultdict(str)
newDict['name'] = '13'
newDict['age'] = '12'
newDict['school'] = '8'
print(newDict)

#now try passing the non available key

print(newDict['name'])
print(newDict['gender'])

'''point to remember :

In your example, you are creating a defaultdict with a default 
factory of int, but then you are immediately reassigning it with a regular dictionary:

newDict = defaultdict(int)
newDict = {'name' : 13, 'age' : 12, 'school' : 8}

So, the defaultdict behavior is lost in this case.

If you want to use defaultdict with a default value of int, 
you should add values using the defaultdict itself:

newDict = defaultdict(int)
newDict['name'] = 13
newDict['age'] = 12
newDict['school'] = 8

'''