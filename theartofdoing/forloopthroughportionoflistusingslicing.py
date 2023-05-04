#list slicing

numbers = list(range(1,12))
for num in numbers:
    print(num)

#[0:5] means start at index 0 print up to index 4 and do not include index 5...the defaul values are [index 0: last element in the list]
print("slicing")
for num in numbers[0:5]:
    print(num)

#how to copy a list
new_numbers = numbers[:] #this copies numbers from index 0 to the last
print(numbers)
print(new_numbers)

numbers.pop()
print(numbers)
print(new_numbers)

names = ["Peter","Kwasi","Kwame","Esi"]
new_names = names.copy()
print(names)
print(new_names)

names.pop()
print(names)
print(new_names)


