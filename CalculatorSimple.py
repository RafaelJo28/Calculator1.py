a= float(input("Enter Value A: "))
b= float(input("Enter Value B: "))
calculator= input("Choose operation: ")

if calculator == "+":
    print(a + b)
    
if calculator == "-":
    print(a - b)
    
if calculator == "x":
    print(a * b)
    
if calculator == "^":
    print(a ** b)
    
if calculator == "/":
    print(a / b)
    
if calculator == "//":
    print(a // b)
    
if calculator == "remainder":
    print(a % b)
