def add(): # without argument and witout return
    print("Adding two numbers")
    
def add1(): #without argument with return
    return 5

def add2(a,b): #with argument no return (a,b are perameter variables)
    print(a+b)
    
def add3(a,b=2):  #with argument no return (a,b = 2  are perameter variables) 
    print(a+b)
    
def add4(a,b): # with argument with return
    return a+b

add() # calling funtion
a = add1() # calling funtion
print(a)

print(add1()) # call directly

add2(2,3) 

add3(2) #default 

add3(2,5) #with a differnt parameter

print(add4(2,3)) #direct call
