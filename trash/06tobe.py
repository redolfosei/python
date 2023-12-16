# Write a program that repeatedly asks the user to enter product names and prices. 
# Store all of these in a dictionary whose keys are the product names and whose values are the prices. 
# When the user is done entering products and prices, 
# allow them to repeatedly enter a product name and print the corresponding price or a message 
# if the product is not in the dictionary.

products = {}

i = 0
for i in range(5):
    product_name = input("Enter the name of product: ")
    product_price = input("Enter product price here: ")
    
    products[product_name] = product_price
    
print(f"These are all products and prices you enter: {products}")

for i in range(5):
    product_name = input("Enter the name of product: ")
    if product_name in products:
        print(products)
    else:
        print(f"The {product_name} you entered is not found in here: ")
        
        

 