# python _54accumulate.itertools.py


from itertools import accumulate
import operator

myList = [1, 2, 3, 4, 5]

res1 = accumulate(myList)
print(list(res1))

#we kept on adding can we do multiplication --yes
# Use a different name for the result of accumulate with multiplication
acc_multiply = accumulate(myList, func=operator.mul)
print(list(acc_multiply))

#similarly we can use all operators max, min, add, mul, sub etc



