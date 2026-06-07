#Class = LeaveBalance
#Attributes = leave_balance private
#leave_balance in list of dictionary
#dictionary contain = name, leave_type,total_leaves,remaining_leaves
#private method to (add_leave,deduct_leave,get_leave_balance) and public method to get leave balance and set balance

class LeaveBalance:
    def __init__(self):
        self.__leave_balance = []           #private attribute

    def __add_leave(self, name, leave_type, total_leaves):
         data = {
              "name": name,
              "leave_type": leave_type,
              "total_leaves": total_leaves,
              "remaining_leaves": total_leaves
         }
         self.__leave_balance.append(data)

    def __deduct_leave(self,name, leave_type, days):
        for record in self.__leave_balance:
            if record["name"] == name and record["leave_type"] == leave_type:
                if record["remaining_leaves"] >= days:
                    record["remaining_leaves"] -= days
                else:
                    print("Not enough leave balance. ")
                return
            print("Record not found. ")

    def __get_leave_balance(self):
        return self.__leave_balance
    
    def add_leave(self, name, leave_type, total_leaves):
        self.__add_leave(name, leave_type,total_leaves)
    
    def deduct_leave(self, name, leave_type, days):
        self.__deduct_leave(name, leave_type, days)

    def display_balance(self):
        records = self.__get_leave_balance()
        if not records:
            print("No leave record found. ")
        else:
            for record in records:
                print(record)

leaveb = LeaveBalance()

leaveb.add_leave("Ram", "Sick", 3)
leaveb.add_leave("Shyam", "Casual", 5)

leaveb.deduct_leave("Ram", "Sick", 11)

leaveb.display_balance()


