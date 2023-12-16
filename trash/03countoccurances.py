# '''RACK YOUR BRAIN.

# Write a function that accepts an id number and return a count
# of each digit in the number

# Eg: id = 11223

# returns
# 1-2
# 2-2
# 3-2
# 4-1

def count_occurance(id_num):

    digit_counts = {}

    for digit in str(id_num):
        if digit in digit_counts:
            digit_counts[digit] += 1
        else:
            digit_counts[digit] = 1

    return digit_counts

digit_counts = count_occurance(1122344566788999999999122333444)

print(digit_counts)

for key, value in digit_counts.items():
    print(f"{key} - {value}")
