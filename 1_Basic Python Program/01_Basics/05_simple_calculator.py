# ============================================================
# Chapter 1 - Simple Calculator
# Topics: if/elif/else, float input, arithmetic operators
# ============================================================

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Choose operator: +, -, *, /")
operator = input("Enter operator: ")

if operator == '+':
    print("Addition =", a + b)
elif operator == '-':
    print("Subtraction =", a - b)
elif operator == '*':
    print("Multiplication =", a * b)
elif operator == '/':
    if b == 0:
        print("Cannot divide by zero.")
    else:
        print("Division =", a / b)
else:
    print("Invalid operator.")

print("Thank you!")
