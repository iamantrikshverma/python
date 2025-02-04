'''
Title: Fibonacci Series

'''
# Fibonacci Series
n1, n2 = 0, 1
count = 0
while count < 10:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count+= 1
  
    