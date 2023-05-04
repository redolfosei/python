print("\n Enter DEPOSIT here: ")
deposit = input()

print("\n Enter WITHDRAW here: ")
withdraw = input()

print("\n Enter PROFIT here: ")
profit = input()

print("\n Enter FEE here:")
fee = input()

customerBalance = int(deposit) + int(profit) - int(withdraw) - int(fee)

print("\n This is the customer's actual balance  " + str(customerBalance))
