#_41DictionariesInter.py

#create an empty dictionary

sampleDict = {}
print(sampleDict, type(sampleDict), 'sample Dictionary')

sampleDict1 = {'eswar'}
print(sampleDict1, type(sampleDict1), 'sample Dictionary 1')
#answer : {'eswar'} <class 'set'> sample Dictionary 1

#what if we needed set but gave the empty brackets
#so we use :

sampleDict2 = dict()
print(sampleDict2, type(sampleDict2), 'sample Dictionary 2')

#and for set we do 

sampleDict3 = set()
print(sampleDict3, type(sampleDict3), 'sample Dictionary 3')

#now we can push data into the dictionary

sampleDict2['name'] = 'eswar'
sampleDict2['age'] = 12

print(sampleDict2, 'sample Dictionary 2 after adding data') 

#generally we created a filled dictionary like 
sampleObj = {'name' : 'eswar', 'age' : 12, 'school' : 'pvhs'}
print(sampleObj['name'])

#but we can also use :
sampleObj1 = dict(name = 'sai', age = 20, school = 'hitech', nickname = 'nami')
print(sampleObj1['name'])

#we have seen we can find the 
#union of sets
#non union of sets
#subtraction of sets but can we do for dictionaries

#print(sampleObj & sampleObj1, 'union of dict')
'''not reasonable it key : value 
we can check the keys but not the values'''
'''so we dont need unions and non-unions and subtractions'''

sampleObj.update(sampleObj1)
print(sampleObj, 'update')


#now that we have been sending int, strings as keys and values
#can we send the lists and tuples as key value pairs

#checking
myDict = dict();
myTuple = (3,2)
myList = [3,3]
myDict['name'] = 'eswar'  #we can send string number as key and value
myDict[myTuple] = 6       #we can send tuple as key
#myDict[myList] = 9       #we cannot send list as key
myDict['tuple'] = myTuple #we can send tuple as value
myDict['list'] = myList   #we can send list as key
print(myDict, 'my dict')
#answer : {'name': 'eswar', (3, 2): 6, 'tuple': (3, 2), 'list': [3, 3]} my dict

myDict['name'] = 'kumar'
print(myDict, 'my dict')


