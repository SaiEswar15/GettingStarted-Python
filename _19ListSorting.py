array = ["eswar", "kumar", "Apple", "Zanana"]
array1 = ["eswar", "kumar", "Apple", "Zanana"]
array2 = [8,3,0,4,6,8]

#sorting will happen alphabetically but capitals first and small next
array.sort();
print(array)

#sorting alphabetically ignoring the case sensitivity
array1.sort(key=str.lower)
print(array1)

array1.sort(key=str.lower, reverse=True)
print(array1)

#sorting numbers increasing order
array2.sort();
print(array2)

array2.sort(reverse=True);
print(array2)

