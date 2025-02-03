ch = ord("A")
h = ord("A")
k, j, m = 0, 0, 0
while k < 7:
    while j < 7:
        if k < j:
            print(" ", end="")
        else:
            if ch > ord("Z"):
                print(" ", end="")
            else:
                print(chr(ch), end="") 
                    
            ch += 1
        j += 1
    j = 0  # Reset j for the next row
    
    # Adjust spacing to create a proper mirror image
    while m < 7:
        if m < (6 - k):  # Adjust the spacing logic here
            print(" ", end="")
        else:
            if h > ord("Z"):
                print(" ", end="")
            else:
                print(chr(h), end="")
            
            h += 1
        m += 1
    m = 0  # Reset m for the next row
    
    print()
    k += 1
    
    
    
    

# rows = 3  # Number of rows
# ch = ord('A')  # Start with ASCII of 'A'

# for i in range(rows):
#     # Print leading spaces for right alignment
#     for space in range(rows - i - 1):
#         print(" ", end="")

#     # Print characters in reverse order
#     temp_ch = ch + i  # Track starting character for each row
#     for j in range(i + 1):
#         print(chr(temp_ch), end="")
#         temp_ch -= 1  # Move backward in characters

#     print()  # Move to the next line