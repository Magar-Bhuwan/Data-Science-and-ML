# create a MRO
# create class A,B,C,D,E
# A,B,C,D,E should inherit from each other in a way that MRO is A,B,C,D,E
# Each class should have a __init__ method that prints the class name
#code for print class name is print(self.__class__.__name__)

class E:
    def __init__(self):
        print(self.__class__.__name__)

class D(E):
    def __init__(self):
        print(self.__class__.__name__)
        super().__init__()

class C(D,E):
    def __init__(self):
        print(self.__class__.__name__)
        super().__init__()

class B(C,D):
    def __init__(self):
        print(self.__class__.__name__)
        super().__init__()

class A(B,C):
    def __init__(self):
        print(self.__class__.__name__)
        super().__init__()

print(A.__mro__)

