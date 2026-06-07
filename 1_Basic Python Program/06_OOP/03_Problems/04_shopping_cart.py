#create class = Cart attributes like items which should be private attribute
# methods like add_item to add item to cart, remove_item to remove item from cart and 
# display_items to display all items in cart

class Cart:
    def __init__(self):
        self.__items = []

    def add_item(self,item):
        self.__items.append(item)

    def remove_item(self,item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print(f'{item} not found in cart. ')

    def display_items(self):
        if not self.__items:
            print("Cart is empty. ")
        else:
            print("Items in Cart. ")
            for item in self.__items:
                print(item)
cart = Cart()

cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Mango")
cart.add_item("Grapes")

cart.display_items()

cart.remove_item("Banana")
cart.display_items()