#for loop 

arr = [1, 4, 6, 3, 12, 0]

#loop each element
for i in arr:
    print(i)

print("""


""")

#loop each index
for i in range(len(arr)):
    print(i)

print("""


""")   

#print both index and values using for loop
for index,i in enumerate(arr):
    print(index, i)

print("""


""") 

#while loop

count = 1

while count<3:
    print(count)
    count+=1

print("while")