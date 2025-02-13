class stack1:
    def __init__(self):
        self.stack = []
        
    
    def topToBottom(self,item):
        self.stack.append(item)
        
        
    def displayStack(self):
        print(self.stack)


s1 = stack1()
s1.topToBottom(10)
s1.topToBottom(20)
s1.topToBottom(30)
s1.displayStack()

# print stack top to bottom without modify original
def printStack(stack):
    stack_copy = stack.copy()
    while stack_copy:
        print(stack_copy.pop(), end=" ")
        

printStack(s1.stack)
print()
# function for print bottom to top without modify original 
def printStackBottomToTop(stack):
    stack_copy = stack.copy()
    s2 = []
    print(stack_copy)
    while stack_copy:
        s2.append(stack_copy.pop())
    while s2:
        print(s2.pop(), end=" ")
                
printStackBottomToTop(s1.stack)

# function for search items in stack

def searchStack(stack, item):
    for i in stack:
        if i == item:
            return True
        return False
        
print(searchStack(s1.stack,10))
print(s1.stack)