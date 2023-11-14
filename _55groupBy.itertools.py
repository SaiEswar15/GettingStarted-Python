# python _55groupBy.itertools.py

#we want to group by certain category this is useful 

from itertools import groupby

def lessThanThree(num):
    return num<3


myList = [1,2,3,4]
result = groupby(myList, key = lessThanThree)  #should pass certain functionality

for i, j in result:
    print(i, list(j))


#can get good hold by this 

info = [{'name':'eswar','age' : 12}, {'name':'sai','age' : 11}, {'name':'kumar','age' : 13}, {'name':'richie','age' : 15}]
result1 = groupby(info, key = lambda x: x['age']<=12)  #should pass certain functionality

for i, j in result1:
    print(i, list(j))