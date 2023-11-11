#remember ++ is not available in python
#global variable cannot be acess by nonlocal keyword
#only local variable can be acessed by nonlocal keyword


"""count = 1

def counter():
    count++;   or nonlocal count
    print(count)

counter();"""

count = 1 

def counter(count):
    #without parameters using
    #nonlocal count (this will give u error)
    #cannot acess global with non local should pass it as parameter
    count += 1
    print(count)

    def solve():
        nonlocal count #here using non-local we can acess the local variable 
        #we can also using by passing it as params
        count = count+1
        print(count)
    
    solve();

counter(count);