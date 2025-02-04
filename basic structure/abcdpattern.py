ch = ord("A")

for i in range(5):
    for j in range(5):
        if (i+j)<=3:
             print(" ", end=" ")
            
        else:
           print(chr(ch), end=" ")
           ch = ch + 1
           
    print()
            