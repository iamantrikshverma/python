class Employee:
    def __init__(self, id,name, age, salary):
        self.id = id
        self.name = name    
        self.age = age
        self.salary = salary

employees =[]

def loadfromfile(filename = 'employee_data.txt'):
    try:
        with open(filename, 'r') as file:
            for line in file:
                id,name,age,salary = line.strip().split(',')
                employee = Employee(id,name,age,salary)
                employees.append(employee)
    except FileExistsError:
        print("File does not exist")
    except Exception as e:
        print(e)

def savetofile(filename = 'employee_data.txt') :
    try:
        with open(filename, 'w') as file:
            for employee in employees:
                file.write(f"{employee.id},{employee.name},{employee.age},{employee.salary}\n")
    except Exception as e:
        print(e)
        
# class for employee managemant system
 
def run(employee):
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee")
        print("4. Display Employees")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            id = input("Enter your id: ")
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            while not age.isdigit():
                age = input("Invalid age. Please enter a valid age: ")
                
                
            salary = input("Enter your salary: ")
            while not salary.isdigit():
                salary = input("Invalid salary. Please enter a valid salary: ")
            emp = Employee(id,name,int(age),float(salary))
            if id in [k.id for k in employees]:
                print("Employee already exists")
            else:
                employees.append(emp)


            

run(employees)              
                
        
            