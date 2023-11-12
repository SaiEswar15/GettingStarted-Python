

arr = [12,3,5,13,9,4]

for index,i in enumerate(arr):
    if(index == 2 or index == 3):
        continue
    print(index,i)

print("loop complete")

for i in arr:
    if (i == 5):
        break
    print(i)

print("loop breaking complete")