#Class = LeaveBalance
#Attributes = leave_balance private
#leave_balance in list of dictionary
#dictionary contain = name, leave_type,total_leaves
#private method to (add_leave,deduct_leave,get_leave_balance) and public method to get leave balance and set leave balance

# class LeaveBalance:
#     def __init__(self):
#         self.__leave_balance = [
#             {
#             'name': "ram",
#             'leave_type': "sick",
#             'total_leave': 10
#             }
#         ]
    
#     def __add_leave(self,dictionary_value):
#         for leave in self.__leave_balance:
#             if leave.get('name') == dictionary_value.geet('name') and leave.get('leave_type') == dictionary_value.get('leave_type'):
#                 leave['total_leaves'] += dictionary_value['total_leaves']
#             else:
#                 return self.__leave_balance.append(dictionary_value)
                
#     def __deduct_leave(self,name,leave_type,days):
#         for record in self.__leave_balance:
#             if record['name'] == name and record['leave_type'] == leave_type:

class LeaveBalance:
    """
    Manages employee leave balances using a private list of dictionaries.

    Private Attribute:
        __leave_balance (list): Each record is a dict with keys:
                                 name, leave_type, total_leaves

    Private Methods:
        __add_leave()         - Add a new leave record
        __deduct_leave()      - Deduct days from an existing record
        __get_leave_balance() - Retrieve records for a specific employee

    Public Methods:
        get_leave_balance()   - Display leave balance for an employee
        set_leave_balance()   - Add or deduct leave (acts as the setter)
    """

    def __init__(self):
        self.__leave_balance = []

    # ------------------------------------------------------------------ #
    #  Private Methods                                                     #
    # ------------------------------------------------------------------ #

    def __add_leave(self, name: str, leave_type: str, total_leaves: int) -> bool:
        """
        Add a new leave record. Prevents duplicate name + leave_type pairs.

        Returns:
            True if added successfully, False if duplicate found.
        """
        for record in self.__leave_balance:
            if record["name"] == name and record["leave_type"] == leave_type:
                print(
                    f"  [!] Record already exists for '{name}' "
                    f"[{leave_type}]. Use 'deduct' action to modify."
                )
                return False

        self.__leave_balance.append({
            "name":         name,
            "leave_type":   leave_type,
            "total_leaves": total_leaves,
        })
        print(
            f"  [+] Added  -> '{name}' | {leave_type} | "
            f"{total_leaves} leave(s) allocated."
        )
        return True

    def __deduct_leave(self, name: str, leave_type: str, days: int) -> bool:
        """
        Deduct leave days from an existing record.

        Returns:
            True if deducted successfully, False otherwise.
        """
        for record in self.__leave_balance:
            if record["name"] == name and record["leave_type"] == leave_type:
                if record["total_leaves"] >= days:
                    record["total_leaves"] -= days
                    print(
                        f"  [-] Deducted -> '{name}' | {leave_type} | "
                        f"{days} day(s) used | "
                        f"Remaining: {record['total_leaves']}"
                    )
                    return True
                else:
                    print(
                        f"  [!] Insufficient balance for '{name}' [{leave_type}] "
                        f"-- Available: {record['total_leaves']}, "
                        f"Requested: {days}"
                    )
                    return False

        print(f"  [!] No record found for '{name}' [{leave_type}].")
        return False

    def __get_leave_balance(self, name: str) -> list:
        """
        Retrieve all leave records for a specific employee.

        Returns:
            List of matching leave-balance dictionaries.
        """
        return [r for r in self.__leave_balance if r["name"] == name]

    # ------------------------------------------------------------------ #
    #  Public Methods                                                      #
    # ------------------------------------------------------------------ #

    def get_leave_balance(self, name: str) -> None:
        """
        Public getter -- display the leave balance for a given employee.

        Args:
            name: Employee name to look up.
        """
        records = self.__get_leave_balance(name)

        print(f"\n{'=' * 44}")
        print(f"  Leave Balance  ->  {name}")
        print(f"{'=' * 44}")

        if not records:
            print(f"  No records found for '{name}'.")
        else:
            print(f"  {'#':<4} {'Leave Type':<20} {'Total Leaves':>12}")
            print(f"  {'-' * 38}")
            for i, rec in enumerate(records, start=1):
                print(
                    f"  {i:<4} {rec['leave_type']:<20} "
                    f"{rec['total_leaves']:>12}"
                )

        print(f"{'=' * 44}\n")

    def set_leave_balance(
        self,
        action: str,
        name: str,
        leave_type: str,
        leaves: int,
    ) -> None:
        """
        Public setter -- add or deduct leave records.

        Args:
            action    : 'add'    -> allocate new leave record
                        'deduct' -> deduct days from existing record
            name      : Employee name
            leave_type: Type of leave (e.g. 'Annual', 'Sick', 'Casual')
            leaves    : Number of leaves to allocate / deduct
        """
        if leaves <= 0:
            print("  [!] 'leaves' must be a positive integer.")
            return

        action = action.strip().lower()

        if action == "add":
            self.__add_leave(name, leave_type, leaves)
        elif action == "deduct":
            self.__deduct_leave(name, leave_type, leaves)
        else:
            print(
                f"  [!] Unknown action '{action}'. "
                "Use 'add' or 'deduct'."
            )


# ====================================================================== #
#  Driver Code                                                            #
# ====================================================================== #

if __name__ == "__main__":

    lb = LeaveBalance()

    # -- Allocate leaves via public setter
    print("\n  SETTING LEAVE BALANCES")
    print("-" * 44)
    lb.set_leave_balance("add", "Alice", "Annual",  20)
    lb.set_leave_balance("add", "Alice", "Sick",    10)
    lb.set_leave_balance("add", "Alice", "Casual",   5)
    lb.set_leave_balance("add", "Bob",   "Annual",  15)
    lb.set_leave_balance("add", "Bob",   "Sick",     8)

    # -- Duplicate guard
    print("\n  DUPLICATE ENTRY TEST")
    print("-" * 44)
    lb.set_leave_balance("add", "Alice", "Annual", 20)

    # -- Read via public getter
    print("\n  GETTING LEAVE BALANCES")
    lb.get_leave_balance("Alice")
    lb.get_leave_balance("Bob")

    # -- Deduct leaves via public setter
    print("\n  DEDUCTING LEAVES")
    print("-" * 44)
    lb.set_leave_balance("deduct", "Alice", "Annual",  5)
    lb.set_leave_balance("deduct", "Bob",   "Sick",    3)

    # Insufficient balance
    lb.set_leave_balance("deduct", "Bob",   "Sick",   10)

    # Non-existent employee
    lb.set_leave_balance("deduct", "Charlie", "Annual", 2)

    # Invalid action
    lb.set_leave_balance("update", "Alice", "Annual", 5)

    # Negative leaves guard
    lb.set_leave_balance("add", "Alice", "Casual", -3)

    # -- Updated balances
    print("\n  UPDATED LEAVE BALANCES")
    lb.get_leave_balance("Alice")
    lb.get_leave_balance("Bob")

    # Non-existent employee
    lb.get_leave_balance("Charlie")