#we will try to write the strings the similar way of lists, dict, tuples, set

#create an empty string 

'''generally we do by'''

string = ''
print(string)

'''what if we try by'''

string1 = str('')
string1 = 'eswar'
print(string1, 'string by method') #this also works if you want to be specific

'''like lists and tuples can we have the slice '''

print(string1[:3], 'slice start to 3rd index')
print(string1[1:], 'slice till last from 1st index')
print(string1[1:3], 'slice middle substring')

#yes we are able to do this slicing

'''like lists and tuples can we have the steps '''

print(string1[::], 'full ')
print(string1[::1], 'every step')
print(string1[::2], 'every 2nd step')
print(string1[::-1], 'reverse the string')

'''access the character of like lists tuples and dict'''

print(string1[0], 'char at 0 index')
print(string1[-1], 'last index')

'''find the length of the string'''

print(len(string1), 'finding the length')

'''lists dictionaries and sets are mutable so they can have 
   myList.append(), myDict['name']='eswar', mySet.add()
   but strings are immutable so there are no such methods like tuples'''


'''can we find the count of elements occuring'''
print(string1.count('e'), 'counting') #this will be seen in tuples

'''can we find the index from where the element starts'''
print(string1.index('w'), 'finding index') #finding the index of substring
print(string1.index('war'), 'finding index')

#difference between find and in is in says only true or false but find gives index

'''will count and index be available in lists lets find out'''
myList = list([2,3,4,5,6,7,2])

print( 2 in myList) #works
print(myList.count(2)) #works
print(myList.index(2)) #works finds the first index of 2
print(myList, type(myList))

'''so they work in strings, lists, tuples also'''

'''in strings we can acess by index but cannot overwrite by index'''

print(string1[0], 'first index by direct access')

'''
lets try updating directly

string1[0] = 's'
print(string1, 'after direct updating') #error has occured

'''

#but we can replace the characters
#above it didnt work because we cannot mutate
#without mutating we can make changes => how?
#by changing the reference of the string and make change

'''
string1.replace('w', 'm')
print(string1) #this may not give you error but it is wrong answer and didnt work'''

#solution :

string1 = string1.replace('w', 'm');
print(string1)

'''string formatting'''

#there are many ways to do : 
#the latest and more readable one is f -strings 

var = 12.253445

print (f'hai i am eswar and i am {var} years old')
#using this we can also make calculations 
print (f'hai i am eswar and i am {round(var)} years old')

#other way is the java way of doing the formatting
print ('hai i am eswar and i am %.2f years old' %var)

#other way is .format method not so useful and readable
print ('hai i am eswar and i am {:.2f} years old'.format(var))