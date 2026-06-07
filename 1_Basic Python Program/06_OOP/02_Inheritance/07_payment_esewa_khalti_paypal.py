""" 
create a class Payment wiht attributes like amount, currency and method pay
create a class that inherits payment named as eSewa
create a class that inherits payment named as Khalti
create a class that inherits payment named as Paypal
each class should have a method pay and use polymorphism in transfer method
each class should have its own transfer charge rate

"""

class Payment:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def Pay(self):
        print(f'{self.amount} {self.currency} is paid')

    def Transfer(self):
        print("Default transfer method")

class Esewa(Payment):
    def __init__(self, amount, currency, charge_rate):
        super().__init__(amount, currency)
        self.charge_rate = charge_rate

    def Transfer(self):
        charge = self.charge_rate
        final_amount = self.amount + charge
        print(f'eSewa Transfer: {final_amount} {self.currency} (Charge: {charge})')

    def Pay(self):
        print(f'{self.amount} {self.currency} paid by eSewa')

class Khalti(Payment):
    def __init__(self, amount, currency, charge_rate):
        super().__init__(amount, currency)
        self.charge_rate = charge_rate

    def Transfer(self):
        charge = self.charge_rate
        final_amount = self.amount + charge
        print(f'Khalti Transfer: {final_amount} {self.currency} (Charge: {charge})')

    def Pay(self):
        print(f'{self.amount} {self.currency} paid by Khalti')

class Paypal(Payment):
    def __init__(self, amount, currency, charge_rate):
        super().__init__(amount, currency)
        self.charge_rate = charge_rate

    def Transfer(self):
        charge = self.charge_rate
        final_amount = self.amount + charge
        print(f'Paypal Transfer: {final_amount} {self.currency} (Charge: {charge})')

    def Pay(self):
        print(f'{self.amount} {self.currency} paid by Paypal')

pay1 = Payment(4000, '$')
pay2 = Esewa(2000, 'NPR', 10)
pay3 = Khalti(1500, 'NPR', 8)
pay4 = Paypal(100, 'USD', 12)

payments = [pay1, pay2, pay3, pay4]

for pay in payments:
    pay.Pay()
    pay.Transfer()