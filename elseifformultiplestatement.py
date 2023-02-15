inputed_number = input('Please specify a number:')
inputed_number = int(inputed_number)
print(inputed_number)

if inputed_number > 0:
    print('The Inputed number ' + str(inputed_number) + ' is bigger than 0')

elif inputed_number == 0:
    print('The inputed_number ' + str(inputed_number) + ' is eaual to 0')
    
else:
    print('The inputed number ' + str(inputed_number) + ' is smaller than 0')
