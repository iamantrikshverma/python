class abc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error! Division by zero is not allowed."
    
    def addition(self,c):
        return self.a + c
    
    # def __str__(self):
    #     return "this is class"
    
    def __repr__(self):
        return "hi"
    
sum = abc(4,5)
print(sum.add())
print(sum.addition(9))
print(sum)

sum2 = abc(4,5)    # new object is not equal to old object
print(sum == sum2)  

print(sum is sum2)  # False, False

sum3 = sum
print(sum is sum3)  # True, True
        
 