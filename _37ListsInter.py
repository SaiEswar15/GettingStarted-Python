#as we already know we can create a list using []

#creating an empty list
arr = []
print(arr)

#creating a non empty list
arr2 = ['eswar', 'kumar']
print(arr2)

#if we want to be specific we can also do 
arr3 = list()
print(arr3)

#if we want to be strict what the variable should hold 
#we can use annotations
#but python will ignore these
arr4 : list = list()
print(arr4, 'with annotation and to be specific')

#list methods 
'''
arr.append(element)   
arr.insert(position, element)
arr.pop()
arr.remove(element)
arr.reverse()
arr.sort()
arr.sort(reverse=True)
arr.sort(key = str.lower)
arr.sort(key = str.lower, reverse=True)
element in arr
len(arr)
arr[0:6]
arr[1:]
arr[:6]
arr.copy()
arr.extend(another array)
arr + anotherArray
sorted(arr)
'''

#steps :

newList1 = [1,2,3,4,5,6,7,8,9]

print(newList1[0::], 'all steps to end')
print(newList1[::1], 'all steps from start')
print(newList1[::2], 'every 2nd step')
print(newList1[2::2], 'every 2nd step from index 2')
print(newList1[::-1], 'all steps to reverse')


'''copying the list

listOrg = [1,3,2,4,22,9]

listnew = listOrg (wrong method)

listnew = listOrg.copy()
listnew = list(listOrg)
listnew = listOrg[:]
'''

#tricks 

zeroArray = [0] * 5
print('zeroArray', zeroArray)

#single line operation for all elements in list
#you want to multiple with itself
sampleList = [1,2,3,4,5,6]
newSampleList = [i*i for i in sampleList]
print(newSampleList)


