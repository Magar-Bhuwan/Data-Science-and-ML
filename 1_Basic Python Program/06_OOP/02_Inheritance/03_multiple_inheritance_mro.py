#multiple inheritance
class GrandMother:
    def __init__(self):
        self.property5 = "Land"

    def height(self):
        print("Height of Grand Mother. ")

class GrandFather:
    def __init__(self):
        self.property6 = "Land"

    def height(self):
        print("Height of Grand Father. ")

class Father:
    def __init__(self):
        self.property1 = "House"
        self.property2 = "Car"

    def height(self):
        print("Height of father. ")

class Mother(GrandMother, GrandFather):
    def __init__(self):
        super().__init__()
        self.property3 = "Gold"
        self.property4 = "Land"
        

class Child(Mother, Father):
    def __init__(self):
        super().__init__()

child1 = Child()

print(child1.property3)
print(child1.property4)

print(child1.height())
        
print(Child.__mro__)