# prime number using function
def is_prime(n):
    if n <= 1:
        print("not a prime number")
    s = 0
    for num in range(2,n): # we are checking from 2 to the number i modulation series if is 0 it mean it divide by something so it would be not a prime number
        if n % num == 0:
            s = 1
    if s == 0 and n != 1:
        print("its a prime number!") # if the number is prime it will print it 
        
    else:
        print("its not a prime number!") # if the number is not prime it will print it
        
#call function
is_prime(9) # it will print its a prime number!