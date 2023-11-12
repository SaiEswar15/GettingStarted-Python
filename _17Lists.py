arr = ["eswar", "kumar", 1, 2, "sai"]

#get elements of the list with index
print(arr[0])

#get the last element in the list
print(arr[len(arr)-1], "element at last index")
print(arr[-1], "element at last index")

#get whether the element is present in list
print("kumar" in arr, "checking")

#changing the element at particular index 
arr[3]="ramu"
print(arr, "updating the value")

#print the length of the list
print(len(arr), "length")

#add elements to the list from the back
arr.append("pen")
print(arr)

#remove elements from the list from the back
print(arr.pop(), "popped element") #gives you the removed element
print(arr, "list after popping")

#slicing the list
print(arr[0:3], "sliced list") #slicing will not effect the original array
print(arr, "list after slicing")

#remove particular elememt from the list
arr1.remove("eswar")
print(arr1, "array after removing particular element")

#merge two lists and get the new list


