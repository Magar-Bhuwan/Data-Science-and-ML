#Define a class Cat and define meowing and print cat behaviour
class Cat:
        def __init__(self,name,bread):
            self.name = name
            self.bread = bread
        def meowing(self):
              return f'{self.name} says meow!'
cat1 = Cat('Kitty','Persion')
cat2 = Cat('Luna','Bengal')

print(cat1.name)
print(cat2.name)
print(cat1.bread)
print(cat2.bread)
print(cat1.meowing())
print(cat2.meowing())