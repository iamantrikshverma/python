# diagonal pattern
# for i in range(5):
#     for j in range(5):
#         if (i == j) or (i+j == 4):
#             print(i+1, end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
            
# plus pattern
# for i in range(3):
#     for j in range(3):
#         if (i == 0 or i == 2) and (j == 0 or j == 2):
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     print()
            
            
# star pattern

for i in range(3):
    for j in range(5):
        if i == 0 :
            if j == 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif (i+j)%2 == 0:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()   

print("me')
