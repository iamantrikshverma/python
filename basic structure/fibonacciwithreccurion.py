def fibonacci(n): # find n is in any fibonacci series using reccursion
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(7))
    
    
def is_n_in_fibonacci(n): #check n in fibonacci series
    index = False
    for i in range(n):
        if fibonacci(i) == n:
            index = True
           
    return index

print(is_n_in_fibonacci(8))