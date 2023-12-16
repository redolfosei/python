""" A class to module a House for sale """
class House():
    def __init__(self, style, sq_footage, year_built, price):
        """ Initialised attributes """
        self.style = style
        self.sq_footage = sq_footage
        self.year_built = year_built
        self.price = price

        self.sold = False
        self.weeks_on_market = 0

    def displayinfo(self):
        print("---\nHouse for sale---")
        print("House style:\t " + str(self.style))
        print("Square Feet:\t" + str(self.sq_footage))
        print("Year Built:\t" + str(self.year_built))
        print("Sales Price:\t" + str(self.price))
        print("\nThis House has been on the market for " + str(self.weeks_on_market) + " weeks.")

    def sell_house(self):
        if self.sold == False:
            print("Congratulations! Your house has sold for $" + str(self.price) + "!")
            self.sold = True
        else:
            print("Sorry, this house is no longer for sale.")

    def change_price(self,amount):
        """ Change price of the house """
        self.price += amount
        if amount < 0:
            print("Price Drop!!")
        else:
            print("The price has increased in value by $" + str(amount) + ".")

    def update_weeks(self, weeks=1):
        """ Increament the number of weeks the house has been on the market """
        self.weeks_on_market += weeks

my_house = House("Ranch", 2000, 2004, 57000)
#print out attributes of the house.
print(my_house.style)
print(my_house.sq_footage)
print(my_house.price)
print(my_house.year_built)

my_house.displayinfo()

#house on market for 1 week
my_house.update_weeks()
my_house.displayinfo()

#house on market for 15 weeks
my_house.update_weeks(15)
my_house.displayinfo()

#change the sale price
my_house.change_price(-7000)
my_house.displayinfo()

#house on market for 5 weeks
my_house.update_weeks(5)
my_house.displayinfo()

#Prices of markets are rising and on demand new interest
my_house.change_price(9000)
my_house.displayinfo()



