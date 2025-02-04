# # prime no 
# for i in range(1,100):
#     s = 0
#     for num in range(2,i): # we are checking from 2 to the number i modulation series if is 0 it mean it divide by something so it would be not a prime number
#         if i % num == 0:
#             s = 1
#     if s == 0 and i != 1:
#         print(i) # if the number is prime it will print it
            
            
# prime no cheacking 
number = input("Enter the number: ")
number = int(number)
for i in range(number, number+1):
    s = 0
    for num in range(2,i): # we are checking from 2 to the number i modulation series if is 0 it mean it divide by something so it would be not a prime number
        if i % num == 0:
            s = 1
    if s == 0 and i != 1:
        print("its a prime number!") # if the number is prime it will print it 
        
    else:
        print("its not a prime number!") # if the number is not prime it will print it