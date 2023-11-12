def outer():
    count = 0
    def inner():
        nonlocal count
        return count+1
    return inner   

inner = outer()
print(inner())