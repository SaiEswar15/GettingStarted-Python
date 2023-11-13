#as we know tuple once fixed cannot be changed

#as we created lists we have no use of creating tuple the same way
#because

newList = list([]) #this can be mutated and changed

#but if we create tuple the same way 

newTuple = tuple(())  #no use we canot mutate it

print(newList)
print(newTuple)  

#both created the list and tuple but there is no use with tuple
#for example :

newList.append('hai')
#newTuple.append('hai') #this doesnt work because there is no method to insert or append the tuple

print(newList)
print(newTuple)  

'''now we will learn keenly about tuple'''

#if we dont use the paranthesis still recognises it as tuple 
#example :

newTuple1 = 'Maven', 'Kotlin', 'Charm'
print(type(newTuple1))  #answer : <class 'tuple'>

#what if hve only one item in tuple
newTuple2 = 'Maven'
print(type(newTuple2))  
#abviously it will become string #answer : <class 'str'>

#this is the reason we use ()
newTuple3 = ('maven')
    #what if we have only one element in tuple
print(type(newTuple3))   #strangely the answer is : <class 'str'>

'''solution'''
newTuple4 = ('maven',)
print(type(newTuple4))   #the answer is : <class 'tuple'>


#'''convert list to tuple'''
newTuple5 = ['maven', 'kotlin', 'android']
newTuple6 = tuple(['maven', 'kotlin', 'android'])
print(newTuple6)

#'''convert tuple to list '''
newTuple7 = ('maven', 'kotlin', 'android')
newTuple8 = list(('maven', 'kotlin', 'android'))
print(newTuple8)


