'''
Title : Student Management System 
Desc: 1- Use list,loop, and Dict.
      2- Take user input
      3- Add student to the list
      4- Display all students
      5- Search student by name 
      6- Delete student by name
      7- courses by student
      8- Exit the program
'''
# Define a dictionary to store students and their courses
students = {}

while 1:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Delete Student by Name")
    print("5. Courses by Student")
    print("6. Exit the Program")
    choice = input("Enter your choice:")
    if choice == '1':
        name = input("Enter Student Name:")
        
        # validation name
        if name in students.keys():
            print("Student already exists")
            continue
        courses = input("Enter courses (comma separated): ") # courses
        courses = courses.split(",") # split courses by comma
        students[name] = courses
        print("Student added successfully")
    elif choice == '2':
        for name, courses in students.items():
            print(name)
    elif choice == '3':
        name = input("Enter Student name: ")
        if name in students.keys():
            print("Student Found")
            print("Courses: ", students[name])
        else:
            print("Student not found!")
    elif choice == '4':
        name = input("Enter Student name: ")
        if name in students.keys():
            students.pop(name) # delete item on key
            print("Student deleted successfully")
        else:
            print("Student not found!")
    elif choice == '5':
        for name, courses in students.items():
            print(name, courses )
    elif choice == '6':
        print("Thankyou For using our system!")
        break
    
    else:
        print("Invalid choice. Please choose a valid option.")
        
        
        
        
        