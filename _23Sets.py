#sets are similar to that of hash set in java
#we cannot pass duplicate into the set
#as in java set doesnt have key value pair and cannot be duplicate

#pass dplicate in the sets and print
newSet = {"eswar", "sai", "kumar", "eswar"}
print(newSet, "duplicates")

#print union of the both the sets #common elements of both sets
newSet1 = {"eswar", "sai", "kumar", "eswar"}
newSet2 = {"Luna", "eswar"}
print(newSet1 & newSet2 , "union or common")

#print non union of the both the sets
print(newSet1 | newSet2, "non-union, not common")

#check if the set1 is subset of set2
newSet3 = {"eswar", "sai", "kumar", "eswar"}
newSet4 = {"sai", "eswar"}
print(newSet4 < newSet3, "is subset")


#find the difference between the sets
print(newSet3-newSet4)