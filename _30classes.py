#class - is nothing by the way of writing object
#contains constructers
#contains variables
#contains functions
#unlike js and java we use self instead of this 
#by using class we can create an object and use the functions and variables inside the object

#initialize class 
#use class keyword and better to use Capital letter to name your class

#we can do inteheritence 
class Animal:
    
    def __init__(self):
        self.legs = 4
        self.eyes = 2
        self.nose = 1
    
class Dogs(Animal):
    def __init__(self, name, breed,noise):
        super().__init__()
        self.name = name
        self.breed = breed
        self.noise = noise

    def sound(self) :
        print(self.name + " is a "+ self.breed + " dog which barks like "+ self.noise + " and has " + str(self.legs) + "legs")



#now using classes create a dogs list with 5 dogs
if __name__ == "__main__":  #this will execute when you execute using this file only
    dogsData = []

    newDog1 = Dogs("Bruno", "Labrador", "woof...")
    newDog2 = Dogs("snoopy", "dalmation", "woow...")
    newDog3 = Dogs("germy", "g shepard", "awwww...")



    dogsData.append(newDog1.__dict__)
    dogsData.append(newDog2.__dict__)
    dogsData.append(newDog3.__dict__)

    print(dogsData)





