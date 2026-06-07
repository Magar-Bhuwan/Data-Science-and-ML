# #create a class for bank account with methods of check_balance
# #attributes like account_number,account_holder_name,balance
# #methods of check_balance

# class Bank:                                                         #Class name --> Bank
#         def __init__(self,account_name,account_number,balance):     #def __init__ (self,...,...,..) constructor
#             self.account_name = account_name                        #account_name --> Public
#             self.account_number = account_number                   #_account_number --> Protected               
#             self.balance = balance                                #__balance --> Private

#         def check_balance(self):                                    #check_balance(self) --> reads the objects stored attributes and return as formating string.
#               return f'Account Holder: {self.account_name}, Account Number: {self.account_number},Balance: {self.balance}'
# acc1 = Bank("Ram", 123, 50000)                                      #Objects/instance --> acc1 which holds the separate data
# acc2 = Bank("Shyam", 235, 60000)                                    #Objects/instance --> acc2 which holds the separate data

# print(acc1.check_balance())                                         #Methods called by acc1 instance
# print(acc2.check_balance())

##Check balance, Deposit and Withdraw
class Bank:                                                         #Class name --> Bank
        def __init__(self,account_name,account_number,balance):     #def __init__ (self,...,...,..) constructor
            self.account_name = account_name                        #account_name --> Public
            self._account_number = account_number                   #_account_number --> Protected
            self.bank_name = 'Nepal Bank'                 
            self.__balance = balance                                #__balance --> Private

        def check_balance(self):                                    #check_balance(self) --> reads the objects stored attributes and return as formating string.
              return self.__balance
        
        def deposit(self, ammount):
              self.__balance += ammount
              return self.__balance
        
        def withdraw(self, ammount):
              if ammount<self.__balance:
                self.__balance -= ammount
                return self.__balance
              else:
                   return 'Balance is not enough. '

acc1 = Bank("Ram", 123, 50000)                                      #Objects/instance --> acc1 which holds the separate data
acc2 = Bank("Shyam", 235, 60000)                                    #Objects/instance --> acc2 which holds the separate data

print(acc1.deposit(100))
print(acc2.deposit(200))

print(acc1.withdraw(51000))
print(acc2.withdraw(500))


