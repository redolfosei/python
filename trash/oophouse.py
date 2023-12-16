class House:
    def __init__(self,style,sq_footage,year_built,price):
        """ Initialising attrubutes """
        self.style = style
        self.sq_footage = sq_footage
        self.year_built = year_built
        self.price = price

        self.sold = False
        self.weeks_on_market = 0

    def displayinfo(self):
        print("--- Information About the House ---")
        print("House Style:\t" + str(self.style))
        print("Square Feet:\t" + str(self.sq_footage))
        print("Year that House was Built:\t" + str(self.year_built))
        print("This house is selling at:\t" + str(self.price))
        print("Number of Week:\t" + self.week_on_market)

    def sell_house(self):
        if self.sold:
            print(f"Congratulation! You sold your house for $ {self.price}")
            self.sold = False
        else:
            print(f"House is still available @ $ {self.price}")

    def change_price(self,amount):
        self.price += amount
        if amount < 0:
            print("Hey! Good news! Price Dropped")
        else:
            print(f"The price has increased by: {amount}")












    
