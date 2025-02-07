class student:
    def __init__(self, student_id, code, test,late):
        self.student_id = student_id
        self.code = code
        self.test = test
        self.late = late
        
    def raw_grade(self):
        total = self.code + self.test
        return total / 2
            
    def final_grade(self):
        a = self.raw_grade()
        return a - self.late
    
    def __str__(self):
        return f"id: {self.student_id}, code: {self.code}, tests: {self.test}, raw:{self.raw_grade()}, late: {self.late}, final:{self.final_grade()}"
    
    

#validation condition
# n = input()
# while not n.isdigit():
#     print("Invalid input. Please enter a number.")
#     n = input()

n = 1
while n > 0 and n < 176:
    code = input("enter code number: ")
    while (not code.isdigit()) or (int(code) < 0 or int(code) > 100):
        print("Invalid Input")
        code = input("enter code number: ") 
    test = input("enter test number: ")
    while (not test.isdigit()) or (int(test) < 0 or int(test) > 100):
        print("Invalid Input")
        test = input("enter test number: ") 
    late = input("enter Late number: ")
    while (not late.isdigit()) or (late not in ['0','1','2']):
        print("Invalid Input")
        late = input("enter late number: ") 
    
    code,test,late = int(code),int(test),int(late)    
    std = student(n,code,test,late)
    print(std)

    k = input("want to check for more student Y or N ")
    if k.upper() == 'Y':
        n+= 1
    else:
        break
    