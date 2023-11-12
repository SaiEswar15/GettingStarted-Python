arr = ["happy", "birthday"]
arr.append("to")
print(arr)

arr2 = arr+["sai", "eswar"]
print(arr2)

arr3 = arr.copy();
print(arr3)

arr4 = arr[:]
print(arr4)

arr.remove("to")
print(arr)

arr.pop();
print(arr)

arr[1:1] = ["new", "year", "to", "you"]
print(arr)

arr.extend(["sai", "eswar"])
print(arr)