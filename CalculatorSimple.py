a= float(input("Enter Value A: "))
b= float(input("Enter Value B: "))
print("+ = Addition")
print("- = Subtraction")
print("x = Multiplication")
print("^ = Exponents")
print("/ = Real Division")
print("// = Floor Division")
print("% = Remainder or Modulo")
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
    
if calculator == "%":
    print(a % b)
