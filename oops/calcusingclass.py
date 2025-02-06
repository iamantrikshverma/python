class calc:
    def __init__(self,a,b):
        self.a = a      #class variable = local variable
        self.b = b 
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        if self.b == 0:
            return "Error: Division by Zero not possible"
        return self.a / self.b
    
    def mod(self):
        if self.b == 0:
            return "Error: Division by Zero not possible"
        return self.a % self.b1
    
    def __str__(self):
        return "calculator!"
    
def options():
    print("choose options: ")
    print("1. Addition")
    print("2.subtraction")
    print("3. Multiplication")
    print("4. divide")
    print("5. mod")
    print("6.exit")
    
    return input("enter your option: ")
    
while True:
    k = options()
    if k in ["1","2","3","4","5"]:
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        cal = calc(a,b)
        if k == "1":
            print("addition:", cal.add())
        elif k == "2":
            print("subtraction:", cal.sub())
        elif k == "3":
            print("multiplication:", cal.mul())
        elif k == "4":
            print("division:", cal.div())
        elif k == "5":
            print("mod :", cal.mod())
    elif k == "6":
        print("Thankyou for using calculator!")
        break
    else:
        print("invalid option")
        
    
            
    
        
    
    
            