
#as we already learnt the method we can access with the creation of tuple

#we already know we cannot append, extend or insert into the tuple
#but we can loop over the tuple, slice the tuple and copy, sort and copy, reverse and copy
#count the occurences of elements in tuple
#find the index of the element

newTuple = (1,3,4,6,7,9,2,3)

#count the occurences of elements in tuple
result1 = newTuple.count(3)
print(result1)

#find the index of the element
result2 = newTuple.index(3)
print(result2)

#finding the length of tuple
print(len(newTuple))

#unpacking tuple
packedTuple = ('eswar', 23, 24)
name, age, date = packedTuple 
    #there should same number of elements to unpack
print(name)   

'''consider if there are more number of elements'''
packedNumberTuple = [1,2,3,4,5,6,7,8,9]
#unpack this tuple
i1, *i2, i3 = packedNumberTuple

print(i1)
print(i2)
print(i3)

