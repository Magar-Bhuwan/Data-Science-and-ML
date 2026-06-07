#inheritance is mainly use to reuse the code and extends functionality of an existing class
#inherit the properties of parent class by child class

# class Animals:
#     def __init__(self,name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} is eating. ')

#     def sleep(self):
#         print(f'{self.name} is sleeping. ')

# class Dog(Animals):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color
#     def bark(self):
#         print(f'{self.name} is barking. ')

# dog1 = Dog("Buddy", "Black")
# print(dog1.color)
# dog1.eat()
# dog1.sleep()
# dog1.bark()

class Animals:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating. ')

    def sleep(self):
        print(f'{self.name} is sleeping. ')

class Bird(Animals):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def fly(self):
        print(f'{self.name} is flying. ')

bird1 = Bird("Sparrow", "Black")
print("Color of bird = ", bird1.color)
bird1.eat()
bird1.sleep()
bird1.fly()


