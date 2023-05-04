numbers = list(range(10,101,10))
print(numbers)

for number in numbers:
    print(number)

squares = []
for n in numbers:
    square = n**2
    squares.append(square)

print("populating Sqaures complete")
for square in squares:
    print(square)
