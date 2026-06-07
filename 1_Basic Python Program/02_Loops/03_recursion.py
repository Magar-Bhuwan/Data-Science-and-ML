# ============================================================
# Loops - Recursion
# Topics: factorial, Fibonacci series
# ============================================================

def fact(n):
    """Returns the factorial of n using recursion."""
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

def fibonacci(n):
    """Returns the nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter a number for factorial: "))
print("Factorial =", fact(num))

num2 = int(input("Enter a positive number for Fibonacci: "))
print("Fibonacci =", fibonacci(num2))
