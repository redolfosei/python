numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# squares = []
# for number in numbers:
#     squares.append(number ** 2)
# print(squares)

#Another way to do this. List Comprehension
# new_squares = [number ** 2 for number in numbers if number % 2 == 0]
# print(new_squares)

#Another way to test for even numbers
# if ((number & 1) == 0)

#Dicrionary comprehension in python
# dict_square = {number: number ** 2 for number in numbers if number % 2 ==0 }
# print("Dict comp: ", dict_square)

#key should be even and value should be odd

# def square(numbers):
#     list1 = []
#     for number in numbers:
#         list1.append(number ** 2)
#     return list1
# print(square(numbers))

#Higher order function in python
#Map, Filter, Reduce, etc functions
# square3 = list(map(lambda x: x ** 2, numbers))
# print(square3)

square4 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print("Square 4 ==> {0}".format(square4))

square5 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print("Square 5 ==> {0} ".format(square5))

array_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = [x for x in array_numbers if x > 4 if x % 2 == 0]
# print(f"These are the results for x ==> {x}")
print(f"This is the results: {results}")

#Nested Loops in a list
matrix = [[1,2,3],[4,15,6],[7,12,9]]
filtered = [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]
print(f"This is the filtered {filtered}")
