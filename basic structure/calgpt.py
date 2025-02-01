a = input("Enter num 1: ")
b = input("Enter num 2: ")

# Check and convert inputs to int or float
if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
    a = float(a) if '.' in a else int(a)
    b = float(b) if '.' in b else int(b)
else:
    print("Invalid input")
    exit()

# Display options
print("\nChoose an operation:")
print("1: Add numbers")
print("2: Subtract numbers")
print("3: Multiply numbers")
print("4: Divide numbers")

# Perform operations
c = input("Your option? ")

if c == '1':
    print(a + b)
elif c == '2':
    print(a - b)
elif c == '3':
    print(a * b)
elif c == '4':
    if b != 0:
        print(a / b)
    else:
        print("Error: Division by zero is undefined.")
else:
    print("Invalid option.")
