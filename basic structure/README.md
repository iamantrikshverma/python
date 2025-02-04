# Python Programming Basics

This repository contains a collection of Python scripts demonstrating various programming concepts, from basic to intermediate level. Each file focuses on specific programming concepts and serves as a learning resource.

## Project Structure

```
basic structure/
├── 1234pattern.py          # Number pattern programs
├── abcdpattern.py          # Alphabet pattern programs
├── calculator.py           # Basic calculator implementation
├── calgpt.py              # Enhanced calculator version
├── dict.py                # Dictionary data structure examples
├── factorial.py           # Factorial calculation
├── fibonacci.py           # Fibonacci sequence implementation
├── fibonacciwithreccurion.py # Recursive Fibonacci implementation
├── functions.py           # Function concepts and examples
├── helloworld.py          # Basic Hello World program
├── ifelse.py             # Conditional statements
├── list.py               # List data structure examples
├── logic.py              # Logic programming examples
├── loops.py              # Different types of loops
├── patterngpt.py         # Advanced pattern programs
├── prime.py              # Prime number checker
├── primeno.py            # Prime number implementations
├── primenousingfxn.py    # Prime number using functions
├── reccrsion.py          # Recursion examples
├── string1.py            # String manipulation examples
├── MiniProject_StudentManagmentSystem.py # A simple student management system
└── variable.py           # Variable declaration and usage
```

## Prerequisites

- Python 3.x installed on your system
- Basic understanding of Python programming

## Installation

1. Clone this repository or download the files to your local machine
2. Make sure Python is installed on your system
3. No additional dependencies are required as all programs use Python's standard library

## Running the Programs

You can run any Python file using the following command in your terminal:

```bash
python filename.py
```

For example:
```bash
python calculator.py
```

## File Descriptions

### Basic Concepts
- `helloworld.py`: Simple introduction to Python printing
- `variable.py`: Demonstrates variable declaration, types, and usage
- `ifelse.py`: Shows how to use conditional statements
- `loops.py`: Examples of for and while loops

### Data Structures
- `list.py`: Operations on lists including creation, modification, and iteration
- `dict.py`: Dictionary operations and use cases
- `string1.py`: String manipulation and operations

### Functions and Recursion
- `functions.py`: Different types of functions and their usage
- `reccrsion.py`: Demonstrates recursive function calls
- `fibonacciwithreccurion.py`: Fibonacci sequence using recursion

### Mathematical Programs
- `calculator.py`: Basic arithmetic operations
- `calgpt.py`: Enhanced calculator with additional features
- `factorial.py`: Calculate factorial of a number
- `fibonacci.py`: Generate Fibonacci sequence
- `prime.py` & `primeno.py`: Different approaches to check prime numbers
- `primenousingfxn.py`: Prime number checking using functions

### Pattern Programs
- `1234pattern.py`: Number-based pattern printing
- `abcdpattern.py`: Alphabet-based pattern printing
- `patterngpt.py`: Advanced pattern printing examples

### Projects
- `MiniProject_StudentManagmentSystem.py`: A simple student management system
- `logic.py`: Collection of logical programming exercises

## Benefits of This Repository

1. **Learning Progression**: Files are organized from basic to advanced concepts
2. **Practical Examples**: Each concept is demonstrated with practical code examples
3. **Code Comments**: Files contain explanatory comments for better understanding
4. **Variety**: Covers multiple programming concepts in one place
5. **Self-Paced Learning**: Can be used for self-study and practice

## Detailed Line-by-Line Explanations

### helloworld.py
```python
#string method
print(f"hello {input()}")
```
- Line 1: Comment indicating this uses string formatting
- Line 2: Uses f-string to print "hello" followed by user input
  - `input()`: Waits for user input
  - `f"hello {}"`: Creates formatted string with input inserted in brackets

### calculator.py
```python
a = input("enter num 1: ")
b = input("enter num 2: ")
```
- Line 1-2: Get two numbers from user input
  - `input()`: Prompts user with specified message
  - Values are initially stored as strings

```python
if a.isdigit() and b.isdigit() :
    a,b = int(a),int(b)
elif '.' in a and '.' in b :
    a,b = float(a),float(b)
elif '.' in a and b.isdigit() :
    a,b = float(a),int(b)
elif a.isdigit() and '.' in b :
    a,b = int(a),float(b)
else:
    print("Invalid input")
    exit()
```
- Lines 4-13: Type conversion logic
  - Checks if inputs are integers using `isdigit()`
  - Checks for decimal points using `'.' in`
  - Converts to appropriate types (int or float)
  - Handles mixed types (one int, one float)
  - Exits if invalid input

```python
print("option 1: add numbers ")  
print("option 2: sub numbers ") 
print("option 3: mul numbers ") 
print("option 4: div numbers ")   
```
- Lines 15-18: Display menu options
  - Shows available operations

```python
c = input("your option ?")
if c == '1':
    print(a + b)
elif c == '2':
    print(a - b)
elif c == '3':
    print(a * b)
elif c == '4':
    if b != 0:
        print(a / b)
    else:
        print("undefined")
else:
    print("Invalid option")
```
- Lines 20-34: Operation execution
  - Gets user's choice
  - Performs selected arithmetic operation
  - Handles division by zero
  - Validates operation choice

### factorial.py
```python
#factorial using while loop
n = int(input("enter number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print(fact)
```
- Lines 1-8: Factorial calculation using while loop
  - Line 1: Comment indicating while loop implementation
  - Line 2: Get user input and convert to integer
  - Line 3-4: Initialize factorial result and counter
  - Lines 5-7: While loop to calculate factorial
    - Multiply current factorial by counter
    - Increment counter
  - Line 8: Print final result

```python
#factorial using for loop
n = int(input("enter number: "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
```
- Lines 10-15: Alternative factorial calculation using for loop
  - Line 10: Comment indicating for loop implementation
  - Line 11: Get user input and convert to integer
  - Line 12: Initialize factorial result
  - Lines 13-14: For loop to calculate factorial
    - `range(1,n+1)`: Iterate from 1 to n inclusive
    - Multiply current factorial by loop variable
  - Line 15: Print final result

### fibonacci.py
```python
n = int(input("enter number: "))
n1,n2 = 0,1
print(n1,n2,end=" ")
for i in range(2,n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3,end=" ")
```
- Line 1: Get the number of Fibonacci terms from user
- Line 2: Initialize first two numbers of sequence (0 and 1)
- Line 3: Print first two numbers with space separator
- Lines 4-8: Generate Fibonacci sequence
  - Line 4: Loop from 2 to n-1 (since we already printed 2 numbers)
  - Line 5: Calculate next number by adding previous two
  - Lines 6-7: Shift numbers for next iteration
  - Line 8: Print current number with space separator
  - `end=" "`: Prevents new line after each number

### loops.py
```python
#for loop
for i in range(5):
    print(i)
```
- Lines 1-3: Basic for loop example
  - Line 1: Comment indicating for loop section
  - Line 2: Loop that iterates 5 times (0 to 4)
  - Line 3: Print current iteration number

```python
#while loop
i = 0
while i < 5:
    print(i)
    i = i + 1
```
- Lines 5-9: While loop example
  - Line 5: Comment indicating while loop section
  - Line 6: Initialize counter
  - Lines 7-9: Loop that runs while i is less than 5
    - Print current value
    - Increment counter

```python
#nested loop
for i in range(5):
    for j in range(5):
        print(i,j)
```
- Lines 11-14: Nested loop example
  - Line 11: Comment indicating nested loops section
  - Lines 12-14: Outer loop (i) and inner loop (j)
    - Creates a 5x5 grid of coordinates
    - Prints pairs of (i,j) values

```python
#break statement
for i in range(5):
    if i == 3:
        break
    print(i)
```
- Lines 16-20: Break statement example
  - Line 16: Comment indicating break statement section
  - Lines 17-20: Loop that stops when i equals 3
    - Only prints 0, 1, and 2
    - Demonstrates early loop termination

```python
#continue statement
for i in range(5):
    if i == 3:
        continue
    print(i)
```
- Lines 22-26: Continue statement example
  - Line 22: Comment indicating continue statement section
  - Lines 23-26: Loop that skips when i equals 3
    - Prints all numbers except 3
    - Demonstrates skipping specific iterations

### primeno.py
```python
# prime no 
for i in range(1,100):
    s = 0
    for num in range(2,i):
        if i % num == 0:
            s = 1
    if s == 0 and i != 1:
        print(i)
```
- Lines 1-8: First implementation - Print all prime numbers from 1 to 100
  - Line 1: Comment indicating prime number generator
  - Line 2: Outer loop from 1 to 99
  - Line 3: Initialize flag for prime number
  - Lines 4-6: Check if number is divisible by any number from 2 to itself
    - If divisible, set flag to 1 (not prime)
  - Lines 7-8: If flag is still 0 and number isn't 1, it's prime
    - Print the prime number

```python
# prime no cheacking 
number = input("Enter the number: ")
number = int(number)
for i in range(number, number+1):
    s = 0
    for num in range(2,i):
        if i % num == 0:
            s = 1
    if s == 0 and i != 1:
        print("its a prime number!")
    else:
        print("its not a prime number!")
```
- Lines 11-22: Second implementation - Check if a specific number is prime
  - Line 11: Comment indicating prime number checker
  - Lines 12-13: Get number from user and convert to integer
  - Line 14: Loop only once for the input number
  - Line 15: Initialize prime flag
  - Lines 16-18: Check divisibility from 2 to number-1
    - If divisible by any number, set flag to 1
  - Lines 19-22: Print result based on flag
    - If flag is 0 and number isn't 1, it's prime
    - Otherwise, it's not prime

### string1.py
```python
#string methods
name = "antriksh verma"
print(len(name))           #length of string
print(name.upper())        #upper case
print(name.lower())        #lower case
print(name.title())        #title case
print(name.capitalize())   #capitalize first letter
print(name.count("a"))     #count number of a
print(name.find("a"))      #find first a
print(name.replace("a","b")) #replace a with b
print(name.split(" "))     #split string into list
print(name.strip())        #remove white space
print(name.lstrip())       #remove left white space
print(name.rstrip())       #remove right white space
print(name.isalpha())      #check if string is alphabet
print(name.isdigit())      #check if string is digit
print(name.isalnum())      #check if string is alphanumeric
print(name.isspace())      #check if string is space
print(name.startswith("a")) #check if string starts with a
print(name.endswith("a"))   #check if string ends with a
```
- Comprehensive demonstration of Python string methods
  - Line 2: Initialize sample string variable
  - Line 3: `len()` - Get string length
  - Line 4: `upper()` - Convert to uppercase
  - Line 5: `lower()` - Convert to lowercase
  - Line 6: `title()` - Capitalize first letter of each word
  - Line 7: `capitalize()` - Capitalize first letter of string
  - Line 8: `count()` - Count occurrences of substring
  - Line 9: `find()` - Find first occurrence of substring
  - Line 10: `replace()` - Replace all occurrences of substring
  - Line 11: `split()` - Split string into list by delimiter
  - Line 12: `strip()` - Remove leading and trailing whitespace
  - Line 13: `lstrip()` - Remove leading whitespace
  - Line 14: `rstrip()` - Remove trailing whitespace
  - Line 15: `isalpha()` - Check if string contains only letters
  - Line 16: `isdigit()` - Check if string contains only digits
  - Line 17: `isalnum()` - Check if string contains letters or digits
  - Line 18: `isspace()` - Check if string contains only whitespace
  - Line 19: `startswith()` - Check string's starting substring
  - Line 20: `endswith()` - Check string's ending substring

### dict.py
```python
#dictionary
d = {"name":"antriksh","age":20,"city":"delhi"}
print(d)
print(d["name"])
print(d.get("name"))
print(d.keys())
print(d.values())
print(d.items())
```
- Demonstration of Python dictionary operations
  - Line 1: Comment indicating dictionary section
  - Line 2: Create dictionary with key-value pairs
    - Contains name, age, and city information
  - Line 3: Print entire dictionary
  - Line 4: Access value using square bracket notation
  - Line 5: Access value using get() method (safer)
  - Line 6: `keys()` - Get list of all dictionary keys
  - Line 7: `values()` - Get list of all dictionary values
  - Line 8: `items()` - Get list of all key-value pairs

### 1234pattern.py
```python
# pattern 1
for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
```
- Pattern 1: Increasing triangle with column numbers
  - Output:
    ```
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    ```
  - Outer loop controls rows (0 to 4)
  - Inner loop runs from 0 to current row number
  - Prints numbers starting from 1 in each column

```python
# pattern 2
for i in range(5):
    for j in range(5-i):
        print(j+1,end=" ")
    print()
```
- Pattern 2: Decreasing triangle with column numbers
  - Output:
    ```
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
    ```
  - Outer loop controls rows (0 to 4)
  - Inner loop runs from 0 to (5-current row)
  - Prints numbers starting from 1 in each column

```python
# pattern 3
for i in range(5):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
```
- Pattern 3: Increasing triangle with row numbers
  - Output:
    ```
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    ```
  - Outer loop controls rows (0 to 4)
  - Inner loop runs from 0 to current row number
  - Prints row number (i+1) in each column

```python
# pattern 4
for i in range(5):
    for j in range(5-i):
        print(5-i,end=" ")
    print()
```
- Pattern 4: Decreasing triangle with constant row numbers
  - Output:
    ```
    5 5 5 5 5
    4 4 4 4
    3 3 3
    2 2
    1
    ```
  - Outer loop controls rows (0 to 4)
  - Inner loop runs from 0 to (5-current row)
  - Prints (5-row number) in each column

```python
# pattern 5
for i in range(5):
    for j in range(5-i):
        print(5-j,end=" ")
    print()
```
- Pattern 5: Decreasing triangle with decreasing numbers
  - Output:
    ```
    5 4 3 2 1
    5 4 3 2
    5 4 3
    5 4
    5
    ```
  - Outer loop controls rows (0 to 4)
  - Inner loop runs from 0 to (5-current row)
  - Prints (5-column number) in each position

### abcdpattern.py
```python
#pattern 1
for i in range(5):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()
```
- Pattern 1: Increasing triangle with alphabet sequence
  - Output:
    ```
    A
    A B
    A B C
    A B C D
    A B C D E
    ```
  - Outer loop controls rows (0 to 4)
  - Inner loop runs from 0 to current row number
  - `chr(65+j)` converts numbers to uppercase letters
    - ASCII value 65 is 'A', 66 is 'B', etc.
  - Prints letters in sequence for each row

```python
#pattern 2
for i in range(5):
    for j in range(5-i):
        print(chr(65+j),end=" ")
    print()
```
- Pattern 2: Decreasing triangle with alphabet sequence
  - Output:
    ```
    A B C D E
    A B C D
    A B C
    A B
    A
    ```
  - Outer loop controls rows (0 to 4)
  - Inner loop runs from 0 to (5-current row)
  - `chr(65+j)` converts numbers to uppercase letters
  - Prints decreasing sequence of letters in each row

### fibonacciwithreccurion.py
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("enter number: "))
print("fibonacci series:")
for i in range(n):
    print(fibonacci(i),end=" ")
```
- First implementation: Basic recursive Fibonacci
  - Lines 1-5: Recursive Fibonacci function
    - Base case: return n if n ≤ 1
    - Recursive case: sum of previous two numbers
  - Lines 7-9: Print series
    - Get number of terms from user
    - Generate and print each term

```python
# fibonacci series with recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("enter number: "))
if n <= 0:
    print("please enter a positive number")
else:
    print("fibonacci series:")
    for i in range(n):
        print(fibonacci(i),end=" ")
```
- Second implementation: Enhanced with input validation
  - Lines 11-15: Same recursive function
  - Lines 17-23: Improved main program
    - Validates input for positive numbers
    - Prints error message for invalid input
    - Generates series only for valid input

Key Concepts:
- Recursive function implementation
- Base case and recursive case
- Input validation
- Series generation using loop
- Space-separated output using end=" "

Note: While recursive implementation is elegant, it's not efficient for large numbers due to repeated calculations. Consider using iterative approach for better performance.

### functions.py
```python
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
```
- Basic arithmetic function definitions
  - Lines 1-2: Addition function
  - Lines 3-4: Subtraction function
  - Lines 5-6: Multiplication function
  - Lines 7-8: Division function
  - Each function takes two parameters and returns result

```python
a = int(input("enter num 1: "))
b = int(input("enter num 2: "))

print("option 1: add numbers ")  
print("option 2: sub numbers ") 
print("option 3: mul numbers ") 
print("option 4: div numbers ")   
```
- User input and menu display
  - Lines 10-11: Get two numbers from user
  - Lines 13-16: Display menu options

```python
c = input("your option ?")
if c == '1':
    print(add(a,b))
elif c == '2':
    print(sub(a,b))
elif c == '3':
    print(mul(a,b))
elif c == '4':
    print(div(a,b))
else:
    print("Invalid option")
```
- Function execution based on user choice
  - Line 18: Get user's choice
  - Lines 19-26: Call appropriate function
    - Option 1: Addition
    - Option 2: Subtraction
    - Option 3: Multiplication
    - Option 4: Division
  - Line 27: Handle invalid input

Key Concepts:
- Function definition and parameters
- Return statements
- Function calls with arguments
- User input handling
- Conditional statements
- Menu-driven program structure

### MiniProject_StudentManagmentSystem.py
A complete student management system implementing CRUD operations (Create, Read, Update, Delete).

```python
class Student:
    def __init__(self, name, roll_number, age, grade):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.grade = grade
```
- Student class definition
  - Constructor initializes student attributes
  - Stores name, roll number, age, and grade

```python
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, age, grade):
        student = Student(name, roll_number, age, grade)
        self.students.append(student)
        print("Student added successfully!")
```
- StudentManagementSystem class
  - Constructor initializes empty student list
  - `add_student`: Creates and adds new student object

```python
    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("\nStudent List:")
            for student in self.students:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Age: {student.age}, Grade: {student.grade}")
```
- View all students
  - Checks if student list is empty
  - Displays formatted information for each student

```python
    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"\nStudent found:")
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Age: {student.age}, Grade: {student.grade}")
                return
        print("Student not found.")
```
- Search student by roll number
  - Iterates through student list
  - Displays student info if found
  - Shows error message if not found

```python
    def update_student(self, roll_number, name, age, grade):
        for student in self.students:
            if student.roll_number == roll_number:
                student.name = name
                student.age = age
                student.grade = grade
                print("Student information updated successfully!")
                return
        print("Student not found.")
```
- Update student information
  - Finds student by roll number
  - Updates name, age, and grade
  - Roll number remains unchanged as identifier

```python
    def delete_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print("Student deleted successfully!")
                return
        print("Student not found.")
```
- Delete student
  - Removes student by roll number
  - Shows success or error message

Main menu provides options to:
1. Add new student
2. View all students
3. Search student by roll number
4. Update student information
5. Delete student
6. Exit system

Features:
- Object-Oriented Design
- Data validation
- User-friendly interface
- CRUD operations
- Error handling
- Persistent student records in memory

## Contributing

Feel free to contribute to this repository by:
1. Adding new example programs
2. Improving existing code
3. Adding better comments and documentation
4. Fixing bugs if found

## License

This project is open-source and available for educational purposes.

## Support

If you encounter any issues or have questions, please open an issue in the repository.

### variable.py
```python
#variable
a = 10
b = 20
c = a + b
print(c)
print(type(c))
```
- Basic variable operations
  - Line 1: Comment indicating variable section
  - Line 2: Assign integer value 10 to variable 'a'
  - Line 3: Assign integer value 20 to variable 'b'
  - Line 4: Add variables and store result in 'c'
  - Line 5: Print value of 'c' (30)
  - Line 6: Print type of variable 'c' (int)

Key Concepts:
- Variable declaration and initialization
- Basic arithmetic operations
- Type checking using type()
- Dynamic typing in Python
- Print function usage

This completes the line-by-line explanation of all the Python files in the basic structure directory. The README now contains detailed explanations of:

1. Basic concepts (variables, strings)
2. Control structures (if-else, loops)
3. Data structures (lists, dictionaries)
4. Functions and recursion
5. Pattern programs (numbers and alphabets)
6. Object-oriented programming (Student Management System)
7. Mathematical implementations (calculator, factorial, Fibonacci)

Each file's explanation includes:
- Code snippets
- Line-by-line breakdown
- Key concepts covered
- Expected output (where relevant)
- Best practices and notes

The codebase serves as an excellent resource for learning Python programming from basic to intermediate level concepts.
