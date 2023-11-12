#tuples are similar to lists 
#but tuples are immutable and cannot be modified like lists
#we cannot insert or remove elements from the tuple
#we can sort the tuple 
#the difference is tuples are opened with () and lists are opened with []

arr = ("sai", "eswar", "Kumar")

#tuple doesnt have sort function #but it has access to sorted function
print(sorted(arr, key=str.lower, reverse=True));

#find at what index what element is present
print(arr.index("eswar"));

#find first elememt in the tuple
print(arr[0])
print(arr[-1])
print(len(arr))

