a = input("enter num 1: ")
b = input("enter num 2: ")

if a.isdigit() and b.isdigit() :
    a,b = int(a),int(b)
elif '.' in a and '.' in b :
    a,b = float(a),float(b)
elif '.' in a and b.isdigit() :
    a,b = float(a),int(b) #float and int coditions
elif a.isdigit() and '.' in b :
    a,b = int(a),float(b) #float and int coditions
else:
    print("Invalid input")
    exit()

print("option 1: add numbers ")  
print("option 2: sub numbers ") 
print("option 3: mul numbers ") 
print("option 4: div numbers ")   

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