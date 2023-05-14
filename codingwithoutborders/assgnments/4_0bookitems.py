class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    #method to add item to menu
    def add_item_to_menu(self,item_name,item_price):
        self.menu_items[item_name] = item_price

    #method to book tables
    def book_table(self,table_no):
        self.book_table.append(table_no)

    #method to take customer orders
    def customer_order(self,order):
        self.customer_orders.append(order)

    #method to print menu
    def print_menu(self):
        for item in self.menu_items:
            print('Item name : {}, item price : {}'.format(item,self.menu_items[item]))

    #method to print table reservations
    def print_table_reservations(self):
        print('Table reservations : {}'.format(self.book_table))