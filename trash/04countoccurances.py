# of each digit in the number

# Eg: id = 11223

# returns
# 1-2
# 2-2
# 3-2
# 4-1

id_number = 1122344566788999999999122333444

str_id_number = str(id_number)

one = str_id_number.count("1")
two = str_id_number.count("2")
three = str_id_number.count("3")
four = str_id_number.count("4")
five = str_id_number.count("5")
six = str_id_number.count("6")
seven = str_id_number.count("7")
eight = str_id_number.count("8")
nine = str_id_number.count("9")
zero = str_id_number.count("0")

print(f"1 - {one}")
print(f"2 - {two}")
print(f"3 - {three}")
print(f"4 - {four}")
print(f"5 - {five}")
print(f"6 - {six}")
print(f"7 - {seven}")
print(f"8 - {eight}")
print(f"9 - {nine}")
print(f"0 - {zero}")