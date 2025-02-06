# inheritance property

class abc:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def test(self):
        print("i am parent class function")
        
class xyz(abc):
    def __init__(self,a,b,c):
        self.c = c
        super().__init__(a,b)
    
    def test2(self):
        print("i am child class function")
        
        
        
k = xyz(1,2,3)
k.test2()
k.test()

            