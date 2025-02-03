# star pattern
# for i in range(3):
#     for j in range(3):
#         if i<j:
#             print(" ", end="")
#         else:
#             print(i+j+1,end="")
            
#     print() 

# # # abcd pattern
# for i in range(3):
#     for j in range(3):
#         if i<j:
#             print(" ", end="")
#         else:
#             print(chr(ord("A")+i+j),end="")
    
#     print() 

# rows = 6  # Set an appropriate number of rows to reach 'Z'
# for i in range(rows):
#     for j in range(rows):
#         if i < j:
#             print(" ", end="")
#         else:
#             letter = chr(ord("A") + i + j)  # Calculate the letter
#             if ord(letter) > ord("Z"):  # Stop if letter exceeds 'Z'
#                 break  # Exit the inner loop if it goes beyond 'Z'
#             print(letter, end="")
#     print()  # Move to the next line
            
            
# for i in range(6):
#     for j in range(6):
#         if i < j:
#             print(" ", end="")
#         else:
#             letter = chr((ord("A") + i + j - ord("A")) % 26 + ord("A"))
#             print(letter, end="")
#     print()

# ch = ord("A")  # Initialize with ASCII of 'A'

# for i in range(3):  # Number of rows
#     for j in range(i + 1):  # Number of characters in each row
#         print(chr(ch), end="")  # Print the current character
#         ch += 1  # Move to the next character
#     print()  # Move to the next line

# ch = ord("A")  # Initialize with ASCII of 'A'

# for i in range(7):  # Number of rows
#     for j in range(i + 1):  # Number of characters in each row
#         if ch > ord("Z"):
#             break
#         print(chr(ch), end="")  # Print the current character
#         ch += 1  # Move to the next character
#     print()  # Move to the next line after each row


# ch = ord("A")
# k,j = 0,0
# while k < 7:
#     while j< 7:
#         if k<j:
#             print(" ", end="")
#         else:
#             if ch > ord("Z"):
#                 break
#             print(chr(ch),end="") 
                    
#             ch += 1
#         j += 1
#     j=0
#     print()
#     k += 1

ch = ord("A")
h = ord("A")
k,j,m = 0,0,0
while k < 7:
    while j< 7:
        if k<j:
            print(" ", end="")
        else:
            if ch > ord("Z"):
                print(" ", end="")
            else:
                print(chr(ch),end="") 
                    
            ch += 1
        j += 1
    j=0
    while m < 7:
        if (m + k) < 6:
            print(" ", end="")
        else:
            if h > ord("Z"):
                print(" ", end="")
            else:
                print(chr(h),end="")
            
            h += 1
        m += 1
    m=0
    print()
    k += 1