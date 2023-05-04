for num in range(3):
    print(num)

wordplay="This is ganduanaland!"
each_char = list(wordplay)
print(wordplay)
print(each_char)

each_char[0] = "ChangedfromTtome"
print(each_char)

new_word = "5".join(each_char)
print(new_word)

back_to_word = "".join(each_char)
print(back_to_word)

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

cubes = [num**3 for num in numbers]
for cube in cubes:
    print(cube)

print(min(cubes))
print(max(cubes))
print(sum(cubes))
