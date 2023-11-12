

def solve(name = "eswar"):  #default parameters
    print(name)

solve("hai"); #arguments
solve(); 

#updating number variable in function
def changeNumber(value):
    value = 12
    print(value)

value = 13
changeNumber(value)
print(value)

#updating string variable in function
def changeString(value):
    value = "eswar"
    print(value)

valueString = "sai"
changeString(valueString)
print(valueString)

#passing lists into function and updating
def changeList(arrList):
    arrList.append("sai")

arrList = ["eswar", "kumar"]
changeList(arrList)
print(arrList)

#passing tuples into function and updating
def changeTuples(arrTuples):
    arrTuples = ("shutup", "please")
    return arrTuples;

arrTuples = ("eswar", "kumar")
print(changeTuples(arrTuples))
print(arrTuples)

#passing dictionaries into function and updating
def changeDict(obj):
    obj["passion"] = "cricket";
    return obj

obj = {"name" : "eswar", "age" : 12}
print(changeDict(obj))
print(obj)

#passing set into function and updating
def changeSet(obj):
    obj = {"happy", "be", "up"}
    return obj

obj2 = {"name", "eswar", "age", "12"}
print(changeSet(obj2))
print(obj2)

