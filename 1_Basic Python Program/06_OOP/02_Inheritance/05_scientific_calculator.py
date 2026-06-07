#classwork in polymorphism
#create a class for calculator with methods add,subtract,multiply,divide
#create a class for scientific calculator which inherits from calculator and
# has methods power,square_root,multiply with 10 to the power format
#create a class for programmer calculator which inherits from calculator and has methods
# binary_to_decimal,decimal_to_binary

import math

class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def add(self):
        print("Addition =", self.first_number + self.second_number)

    def subtract(self):
        print("Subtraction =", self.first_number - self.second_number)

    def multiply(self):
        print("Multiplication =", self.first_number * self.second_number)

    def divide(self):
        if self.second_number == 0:
            print("Cannot divide by zero")
        else:
            print("Division =", self.first_number / self.second_number)

# Scientific Calculator (Polymorphism)
class Scientific_calc(Calculator):
    def power(self):
        print("Power =", self.first_number ** self.second_number)

    def square_root(self):
        print("Square Root =", math.sqrt(self.first_number))

    # Method Overriding (Polymorphism)
    def multiply(self):
        print(f"{self.first_number} * 10^{self.second_number} = {self.first_number * (10 ** self.second_number)}")

calc = Calculator(10, 5)
sci_calc = Scientific_calc(3, 3)

calc.add()
calc.subtract()
calc.multiply()
calc.divide()
print()

sci_calc.power()
sci_calc.square_root()
sci_calc.multiply()   # polymorphism
print()
