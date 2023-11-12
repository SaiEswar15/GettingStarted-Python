#when you dont want to change the functionality of the function 
#but you want to add functionality before and after the function 
#we can use decorators


def addNumber(func) :
    def wrapper():
        print('before')
        val = func()
        print('after')
        return val
    return wrapper

@addNumber
def solveSquare():
    print('eswar')

solveSquare()
