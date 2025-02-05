#Consider a list (list = []). You can perform the following commands:
# 1 insert i e: Insert integer e at position i:
# 2 print: Print the list.

# start program 
list = []

while True:
    print("1. Insert i e: insert integer e at position i")
    print("2. print1; print the list")
    print("3. remove e: delete the first occurrence of integer e")
    print("4. append e: insert integer e at end of the list")
    print("5. sort: sort the list")
    print("6. pop: pop the last element from the list")
    print("7. reverse: reverse the list")
    print("8. exit program")
    
    choice = input("please select an option!")
    if choice == '1':
        i = int(input("Enter the position: "))
        e = int(input("Enter the integer to be inserted: "))
        list.insert(i, e)
        print("List after insertion: ", list)
    
    elif choice == '2':
        print("List: ", list)
        
    elif choice == '3':
        list.delete(0, e)
        print("List after deletion: ", list)
    elif choice == '4':
        e = int(input("Enter the integer to be inserted: "))
        list.append(-1, e)
        print("List after insertion: ", list)    
    elif choice == '5':
        print("List: ", list.sort())
    elif choice == '6':
        print("List: ", list.pop()) 
    elif choice == '7':
        print("List: ", list.reverse())
    elif choice == '8':
        break
    