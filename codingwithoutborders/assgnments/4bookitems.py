# Question 4
# Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like
# add_item_to_menu, book_tables, and customer_order. Perform the following tasks now: Now add items to the menu. Make
# table reservations. Take customer orders. Print the menu. Print table reservations. Print customer orders. Note:
# Use dictionaries and lists to store the data.

class Restaurant:
    def __init__(self, menu_items, book_table, customer_orders):
        self.menu_items = menu_items
        self.book_table = book_table
        self.customer_orders = customer_orders

    def add_item_to_menu(self):
        self.menu_items = []
        meal = input("Enter an item here: \n")
        self.menu_items.append(meal)
        print(self.menu_items)

    def book_tables(self):
        time = input("Enter the time you would like to come here in O'ClockL: ")
        number_of_seats = input("Enter the of number of seats you would like to reserve here: ")
        self.book_table = input("Enter the number of tables you would like to reserve here: ")
        print("You have booked on {0} O'Clock, reserving {1} number of seats and {2} number of tables".format(time,number_of_seats,self.book_table))

    def customer_order(self):
        order_here = input("Enter you order here: ")
        print("You have ordered {0} here...".format(order_here))

menu_items_1 = Restaurant("","","")
menu_items_1.add_item_to_menu()

book_tables_1 = Restaurant("","","")
book_tables_1.book_tables()

customer_order_1 = Restaurant("","","")
customer_order_1.customer_order()
