obj1 = {"name" : "eswar", "age" : 12, "color" : "red", "lastName" : "pendurthi"}

#get all the keys from the dictionary

print(obj1.keys())
#if wanted to print only the list we can use 
print(list(obj1.keys()))

#get all the values from the dictionary
print(obj1.values())
#if wanted only to print the list of values
print(list(obj1.values()))

#get all the properties 
print(obj1)
print(obj1.items())
#if wanted only to print the list of properties
print(list(obj1.items()))


#copy the dictionary into another dictionary
print(obj1)
obj2 = obj1.copy();
obj2["job"] = "kali"
print(obj1)
print(obj2)