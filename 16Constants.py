#constants in python

#we have to import the Enum from enum and pass it in a class called State

from enum import Enum

class stage(Enum): #we can use any class name with Capital title if not capital also works
    pi = 3.124
    age = 24

#State.pi.value++
#print(State.pi.value)  #constant cannot be changed

print(stage.pi.value)

#print the list of constants 
print(list(stage))

#print the total no of enums or constants present in the class
print(len(stage))
