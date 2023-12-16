# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.

#open file1.txt and save as file1
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

#open file2.txt and save as file2
with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(item) for item in file_1_data if item in file_2_data]

# Write your code above 👆
print(result)


















# f = open("file3.txt", "r")
# f = f.readlines()
# # print(f.readlines())
# print(f)

# f = open("file1.txt", "r")
# print(f.readlines(22))