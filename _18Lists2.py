#adding list to already existing list
arr1 = ["eswar", "sai"]
arr2 = ["kumar", "pendurthi"]
arr3 = ["yup", "rep"]
arr1.extend(arr2) #if we print this line we dont get any output to store in any variable
print(arr1.extend(arr2)) #output : None
arr3 = arr1.extend(arr2) #here it extends but dont print
print(arr3) #output : None
print(arr1)


#insert element at particular index
items = ["vegetables", "fruits", "leafy"]
items.insert(1, "meaty")
print(items)

#insert elements list at particular index
items1 = ["vegetables", "fruits", "leafy"]
items1[1:1] = ["meaty", "juicy", "creamy"]
print(items1, "at particular index")

#merging two arrays/list
items2 = ["vegetables", "fruits", "leafy"]
items3 = items2.copy()
items3.extend(items2)
print(items3, "merge")

#checking 
array = ["hi", "bye"]
array1 = array + ["ko"]  #adding will give you new array
array1.insert(0,"yo")
print(array1)
print(array)