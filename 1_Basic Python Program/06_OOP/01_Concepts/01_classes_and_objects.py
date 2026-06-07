# #Class is a blueprint/collection of data/properties/attributes and methods/behaviour (objects). It doesnot take place memory space. 
# #Object is a instance of class and takes space on memory.
#Simple Example: Class name = Car & Objects = Properties(Car Name, Car Brand,etc) & Methods/ Behaviour(Car Break, Car Speed, etc)
# 
class Dog:                                        #class name is Dog
        def __init__(self,name,brand):            #the __init__ Method (Parameterized Constructor) --> def __init__(self,name,brand)
            self.name = name                      #self refers to the specific object being created.
            self.brand = brand                    #self.name = name --> stores the name of as instance attributes

        def bark(self):              #bark(self) --> methods reads the objects stored attributes and return them as a formating string.
              return f'{self.name} says woof!'
dog1 = Dog('Buddy','Husky')                       #There are two separate instance class dog1 & dog2 and holds different data
print(type(dog1))
dog2 = Dog('Lucky','German Shephard')
print(type(dog2))

print(dog1.name)
print(dog2.name)
print(dog1.bark())                                #Methods called by dog1(class) with bark(methods)
print(dog2.bark())