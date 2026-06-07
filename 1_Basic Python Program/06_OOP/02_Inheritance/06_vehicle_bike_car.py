#create a class vehicle with attributes like: model, year and methods like start_engine,stop_engine
#createa class bike which inherits from vehicle and has attributes like num_wheels
#methods like open_sidebar, close sidebar, start_engine, stop_engine
#create a class car which inherits from vehicle and has attributes like num_doors
#methods like open_doors, close_doors, start_engine, stop_engine

class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def start_engine(self):
        print(f'{self.model} ({self.year}) engine started.')

    def stop_engine(self):
        print(f'{self.model} ({self.year}) engine stopped.')

class Bike(Vehicle):
    def __init__(self, model, year, num_wheels):
        super().__init__(model, year)
        self.num_wheels = num_wheels

    def open_sidebar(self):
        print(f'{self.model} sidebar opened.')

    def close_sidebar(self):
        print(f'{self.model} sidebar closed.')

class Car(Vehicle):
    def __init__(self, model, year, num_doors):
        super().__init__(model, year)
        self.num_doors = num_doors

    def open_doors(self):
        print(f'{self.model} has {self.num_doors} doors opened.')

    def close_doors(self):
        print(f'{self.model} doors closed.')
        
car1 = Car("Corolla", 2022, 4)
bike1 = Bike("CBR", 2020, 2)

car1.start_engine()
car1.stop_engine()
car1.open_doors()
car1.close_doors()

bike1.start_engine()
bike1.stop_engine()
bike1.open_sidebar()
bike1.close_sidebar()