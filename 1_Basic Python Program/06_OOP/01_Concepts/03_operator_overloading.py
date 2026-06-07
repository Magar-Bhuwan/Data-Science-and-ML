
class Numbers:
    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        return self.num - other.num
    
    def __str__(self):
        return str(self.num)
    
n1 = Numbers(10)
n2 = Numbers(20)

print(type(n1))
print(type(n2))
print(type(n1+n2))
print(n1)

result = n1 + n2

print(result)


