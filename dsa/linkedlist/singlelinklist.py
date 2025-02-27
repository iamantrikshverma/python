import os
# Employee Class
class Employee:
    def __init__(self, employee_id, employee_name, employee_position, employee_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_position = employee_position
        self.employee_salary = employee_salary


# Implement a linked list to store Employee objects.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class EmployeeLinkedList:
    def __init__(self):
        self.start = None
        self.loadEmployeeData()

    def checkID(self, employeeID):
        current = self.start
        while current:
            if current.data.employee_id == employeeID:
                return True   
            current = current.next
        return False   
    
    def addEmployee(self, emp):
        new_node = Node(emp)
        if not self.start:
            self.start = new_node
        else:
            current = self.start
            while current.next:
                current = current.next
            current.next = new_node
        self.saveEmployeeData()    
            

    def deleteEmployee(self, employeeID):
        current = self.start
        previous = None
        while current:
            if current.data.employee_id == employeeID:
                if previous:
                    previous.next = current.next
                    
                else:
                    self.start = current.next
                self.saveEmployeeData()
            previous = current
            current = current.next
        
        
    def displayEmployees(self):
        current = self.start
        if not current:
            print("No employees to display.")
            return   
        print("\nEmployee List:")
        while current:
            print(f"Employee ID: {current.data.employee_id}")
            print(f"Name: {current.data.employee_name}")
            print(f"Position: {current.data.employee_position}")
            print(f"Salary: {current.data.employee_salary}")
            current = current.next
    
    
    # save employee data in file
    def saveEmployeeData(self):
        file = open("employee_data.txt", "w")
        current = self.start
        while current:
            file.write(f"{current.data.employee_id}:")
            file.write(f"{current.data.employee_name}:")
            file.write(f"{current.data.employee_position}:")
            file.write(f"{current.data.employee_salary}")
            file.write("\n")
            current = current.next   
        
    # load employee data from file
    def loadEmployeeData(self):
        # create the file if it not there
        if not os.path.exists("employee_data.txt"):
            with open("employee_data.txt", "w") as file:
                # Create the file if it doesn't exist
                pass
            print("⚠ No previous employee data found. Starting fresh.")
            return
        with open("employee_data.txt", "r") as file:
            content = file.read()
            # print(content)
            lines = content.split('\n')[:-1]
            # print(lines)
        
        for line in lines:
            # print("Hi")
            employeeID, employeeName, employeePosition, employeeSalary = line.split(":")
            # employee object
            emp = Employee(int(employeeID),employeeName,employeePosition,float(employeeSalary))
            if self.start is None:
                self.start = Node(emp)
                # print("Hi")
            else:
                self.addEmployee(emp)
            
# Main class that shows employee management system.
class Employee_Management_system:
    def __init__(self):
        self.employees = EmployeeLinkedList()
    
    def run(self):
        while True:
            print("Employee_Management_System")
            print("1. Add a new employee")
            print("2. Delete an employee")
            print("3. Display all employees")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                while True:
                    employee_id = input("Enter employee ID: ")
                    # check employee_id is a number and unique means not exist already
                    if employee_id.isdigit():
                        employee_id = int(employee_id)
                        if self.employees.checkID(employee_id):
                            print("Employee ID already exists. Please enter a unique ID.")
                        else:
                            employee_name = input("Enter employee name: ")
                            employee_position = input("Enter employee position: ")
                            
                        
                            # check employee_salary is a number
                            while True:
                                employee_salary = input("Enter employee salary: ")
                                if employee_salary.replace('.', '', 1).isdigit():
                                    employee_salary = float(employee_salary)
                                else:
                                    print("Invalid employee salary. Please enter a number.")
                                    continue
                                break
                                
                        self.employees.addEmployee(Employee(employee_id, employee_name, employee_position, employee_salary))
                        print("Employee added successfully!")
                    else:
                        print("Invalid employee ID. Please enter a number.")
                        continue
                    break
            # for delete employee
            elif choice == "2":
                employee_id = input("Enter employee ID to delete: ")
                if employee_id.isdigit():
                        employee_id = int(employee_id)
                        if self.employees.checkID(employee_id):
                            self.employees.deleteEmployee(employee_id)
                            print("Employee deleted successfully!")
                        else:
                            print("Employee ID does not exist.")
                else:
                    print("Invalid employee ID. Please enter a number.")
                            
                
            
            # for display all employees
            elif choice == "3":
                self.employees.displayEmployees()
                print("Employees displayed successfully!")
            
            # for exit 
            elif choice == "4":
                print("Thank you for use our system!...")
                break
            else:
                print("Invalid choice. Please try again.")


main1 = Employee_Management_system()
main1.run()
