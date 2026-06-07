try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    result = a/b

except ZeroDivisionError:
    print("cannot divide by zero")

else:
    print(f"Result = {result}")