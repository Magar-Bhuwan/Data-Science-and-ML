#create a class for Vehicle with attributes like make,model,year
#methods like start_engine, stop_engine
#create a class for car which inherits from vehicle and has attributes like num_doors
#methods like open_doors, close_doors
#create a clss for Motorcycle which inherits from vehicle and has attributes like has_sidecar
#methods like open_sidecar, close_sidecar


class Vehicle:
    def __init__(self, make, model,year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f'{self.make} {self.model} ({self.year}) engine started. ')

    def stop_engine(self):
        print(f'{self.make} {self.model} ({self.year}) engine stoped. ')

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def open_doors(self):
        print(f'{self.make} , {self.model} has {self.num_doors} doors opened. ')

    def close_doors(self):
        print(f'{self.make} {self.model} doors closed. ')

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def open_sidecar(self):
        if self.has_sidecar:
            print(f'{self.make} {self.model} sidecar open. ')
        else:
            print(f'{self.make} {self.model} has no sidecar. ')

    def close_sidecar(self):
        if self.has_sidecar:
            print(f'{self.make} {self.model} csidecar closed. ')
        else:
            print(f'{self.make} {self.model} has no sidecar. ')

car1 = Car("Totyota", "Corola", 2022, 4)
bike1 = Motorcycle("Honda", "CBR", 2020, False)

car1.start_engine()
car1.stop_engine()
car1.open_doors()
car1.close_doors()

bike1.start_engine()
bike1.stop_engine()
bike1.open_sidecar()
bike1.close_sidecar()




