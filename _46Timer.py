from timeit import default_timer as timer


myList = ['a'] * 10

print(myList)

#general method to combine the list to string
start = timer()
newString = str('')
for i in myList:
    newString += i

print(newString)
stop = timer()
print(start-stop)

#method using the join method
start = timer()
newString1 = ''.join(myList)

print(newString1)
stop = timer()
print(start-stop)

