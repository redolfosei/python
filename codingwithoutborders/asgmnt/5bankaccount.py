# Question 5
# Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name,
# and methods like create_user_account, deposit, withdraw, and check_balance.

import random

class BankAccount:
    def __init__(self, customer_name):
        self.account_number = str(random.randint(100000000000, 999999999999))
        self.balance = 0
        self.date_of_opening = ""
        self.customer_name = customer_name


    def deposit(self):
        amount = int(input("Enter an amount to deposit here: "))
        self.balance += amount
        print(f"Deposit of {amount} was successful. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful...New Balance is {self.balance}")

    def check_balance(self):
        print("Your account Number is: {0}".format(self.account_number))
        print(f"Your balance is {self.balance} ")


customer1 = BankAccount(input("Enter a name here: \n"))
customer1.check_balance()
customer1.deposit()
customer1.check_balance()
