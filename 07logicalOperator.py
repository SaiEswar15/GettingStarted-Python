#important logical operators 
# and, or , not 
# there are no &&, ||, (!value) like in javascript

print(3 and 4)
print(3 or 4)


number1 = 12
number2 = 13

if(number1<number2 and number1<=number2):
    print("true")
else:
    print("false")


number1 = 12
number2 = 13
if(number1<number2 or number1<=number2):
    print("true")
else:
    print("false")


value1 = 1
if( not value1):
    print("true","valu1")
else:
    print("false","valu1")