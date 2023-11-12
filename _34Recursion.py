#recursion is similar to all languages 
#but should be written in python syntax

def factorial(number) :
    
    #base condition
    if number==0 : 
        return 1
    #least work
    return number*factorial(number-1)

print(factorial(3))



