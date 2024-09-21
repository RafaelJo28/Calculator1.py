try:
    a = float(input("Enter Value A: "))
    b = float(input("Enter Value B: "))
except ValueError:
    print("Please enter valid numbers.")
    exit()

print("\nChoose an operation:")
print("+  = Addition")
print("-  = Subtraction")
print("x  = Multiplication")
print("^  = Exponents")
print("/  = Real Division")
print("// = Floor Division")
print("%  = Remainder or Modulo")

calculator = input("\nChoose operation: ")

if calculator == "+":
    result = a + b
elif calculator == "-":
    result = a - b
elif calculator == "x":
    result = a * b
elif calculator == "^":
    result = a ** b
elif calculator == "/":
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero."
elif calculator == "//":
    if b != 0:
        result = a // b
    else:
        result = "Error: Division by zero."
elif calculator == "%":
    if b != 0:
        result = a % b
    else:
        result = "Error: Division by zero."
else:
    result = "Error: Invalid operation."

print("\nResult:", result)
