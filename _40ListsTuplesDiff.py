#as we have learn both lists and tuples 
#both basics and intermediate

#when to use what 

'''when you have fixed number of elements in array
and need not to mutate and update the elements then we can use tuples'''

'''when your array needs constant updation and mutation and not fixed size 
we can use the lists'''

#which takes the less size 
#we can test by using the getsizeof() method

sampleList = list()
sampleTuple = tuple()

print(sampleList)
print(sampleTuple)

#get size of the both list and tuple

import sys

'''but inorder to get the size we should import sys module'''
print(sys.getsizeof(sampleList), 'bytes')   #answer : 56 bytes
print(sys.getsizeof(sampleTuple), 'bytes')  #answer : 40 bytes

#list takes more time to create then the tuple 
#so they should be used according to the situation