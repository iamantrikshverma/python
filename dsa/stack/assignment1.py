class stack_1:
    def __init__(self):
        self.stack = []



def topToBottom(stack):
    stack_copy = stack.copy()
    print("Stack content:"+" ".join(str(i) for i in stack_copy))
    while stack_copy:
        print(stack_copy.pop(), end=" ")
    
def bottomToTop(stack):
    stack_copy = stack.copy()
    print("Stack content:"+" ".join(str(i) for i in stack_copy))
    s2 = []
    while stack_copy:
        s2.append(stack_copy.pop())
    while s2:
        print(s2.pop(),end=" ")
                
                
                
# function for flip stack
def flipStack(stack):
    s2 = []
    while stack:
        s2.append(stack.pop())
    while s2:
        stack.append(s2.pop())
    print(" ".join(str(i) for i in stack))
            
        
        
# function for search item wether it is present or not
def searchItem(stack, item):
    stack_copy = stack.copy()
    while stack_copy:
        k = stack_copy.pop()
        if k == item:
            print(k)
            return True
    return False
        
# main function that show all these choices and menu 
def main():
    while True:
        print("\n-----MAIN MENU-----")
        print("1. Test function topToBottom with integer stack")
        print("2. Test function bottomToTop with double stack")
        print("3. Test function flipStack with string stack")
        print("4. Test function searchStack with integer stack")
        print("5. Exit program")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            stack = stack_1()
            num = list(map(int, input("Enter integers to push onto the stack separated by space: ").split()))
            
            for n in num:
                stack.stack.append(n)
            topToBottom(stack.stack)
            
        elif choice == '2':
            stack = stack_1()
            num = list(map(float, input("Enter doubles to push onto the stack separated by space: ").split()))
            for n in num:
                stack.stack.append(n)
            bottomToTop(stack.stack)
            
        elif choice == '3':
            stack = stack_1()
            str =  input("Enter strings to push onto the stack separated by space: ").split()
            for s in str:
                stack.stack.append(s)
            flipStack(stack.stack)
        
        elif choice =='4':
            stack = stack_1()
            num = list(map(int, input("Enter integers to push onto the stack separated by space: ").split()))
            stack.stack = num
            num1 = int(input("Enter integers to search in the stack separated by space: "))
            print(searchItem(stack.stack, num1))
        
        elif choice =='5':
            print("Exiting program")
            break
            
        else:
            print("Invalid choice. Please choose a valid option.")
            
            
main()
        
        
        
        