def topToBottom(stack):
    """Displays stack from top to bottom without modifying the stack."""
    temp_stack = stack.copy()
    print("Stack content:", end=" ")
    while temp_stack:
        print(temp_stack.pop(), end=" ")
    print()

def bottomToTop(stack):
    """Displays stack from bottom to top without modifying the stack."""
    temp_stack = stack.copy()
    print("Stack content:", end=" ")
    for item in temp_stack:
        print(str(item), end=" ")
    print()

def flipStack(stack):
    """Flips the stack content and returns the flipped stack."""
    flipped_stack = []
    while stack:
        flipped_stack.append(stack.pop())
    return flipped_stack

def searchStack(stack, target):
    """Searches for target in stack without modifying the stack."""
    return target in stack

def main():
    while True:
        print("\n-----MAIN MENU-----")
        print("1. Test function topToBottom with integer stack")
        print("2. Test function bottomToTop with double stack")
        print("3. Test function flipStack with string stack")
        print("4. Test function searchStack with integer stack")
        print("5. Exit program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Test topToBottom with integer stack
            numbers = list(map(int, input("Enter integers to push onto the stack (space-separated): ").split()))
            stack = []
            for num in numbers:
                stack.append(num)
            print("Stack content:"+" ".join(str(i) for i in stack))
            print("Function output:", end=" ")
            topToBottom(stack)
        
        elif choice == "2":
            # Test bottomToTop with double stack
            numbers = list(map(float, input("Enter doubles to push onto the stack (space-separated): ").split()))
            stack = []
            for num in numbers:
                stack.append(num)
            print("Stack content:", str(stack))
            print("Function output:", end=" ")
            bottomToTop(stack)
        
        elif choice == "3":
            # Test flipStack with string stack
            strings = input("Enter strings to push onto the stack (space-separated): ").split()
            stack = []
            for s in strings:
                stack.append(s)
            print("Stack content before calling flipStack:", str(stack))
            flipped_stack = flipStack(stack)
            print("Stack content after calling flipStack:", flipped_stack)
        
        elif choice == "4":
            # Test searchStack with integer stack
            numbers = list(map(int, input("Enter integers to push onto the stack (space-separated): ").split()))
            stack = []
            for num in numbers:
                stack.append(num)
            print("Stack content:", str(stack))
            target = int(input("Enter target value to search for: "))
            print("Function output:", searchStack(stack, target))
        
        elif choice == "5":
            print("Thank you for using the system!... Exiting.")
            break
        
        else:
            print("Invalid choice. Please try again.")
main()
