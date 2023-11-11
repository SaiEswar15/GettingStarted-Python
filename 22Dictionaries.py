#dictionaries data structure follow the key-value pairs

#{}
#what can we do inside the dictionaries

#create an empty dictionary 
obj = {};
print(obj);

#adding property into the dictionary
obj["name"] = "eswar"
print(obj)

obj["age"] = 12
obj["color"] = "red"
print(obj)

#find if the item is present in the element
print("age" in obj)

#remove property in the dictionary
print(obj.pop("age"))
print(obj)

print(obj.popitem());
print(obj)

del obj["name"]
print(obj , "delete the prop from obj")

#get element from the object

obj1 = {"name" : "eswar", "age" : 12, "color" : "red", "lastName" : "pendurthi"}
print(obj1["name"], "get element");
print(obj1.get("name"), "getting the element by get element");

#advantage of using get function
#we can use default value if property is not present

#if we use 
#print(obj1["month"], "get the month without using get()")
#we get an error so to solve the issue we use the 
obj1["month"] = "June";
print(obj1.get("month", "August"), "using get method and passing default")

