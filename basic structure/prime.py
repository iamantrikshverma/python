x =int( input("Enter a number: "))

# Check for numbers less than 2
if x < 2:
    print(f"{x} is not a prime number.")
# Check for small prime numbers directly
elif x == 2 or x == 3 or x == 5 or x == 7:
    print(f"{x} is a prime number.")
# Check for divisibility by 2, 3, 5, or 7
elif x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
    print(f"{x} is not a prime number.")
else:
    print(f"{x} is a prime number.")