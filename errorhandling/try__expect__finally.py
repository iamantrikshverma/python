# 0/0 
try:
    a = 0
    b = "0"
    c = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed") 

except e:
    print(e)  # This will catch all other exceptions as well