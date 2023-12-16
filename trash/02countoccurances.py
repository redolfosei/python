# '''RACK YOUR BRAIN.

# Write a function that accepts an id number and return a count
# of each digit in the number

# Eg: id = 11223

# returns
# 1-2
# 2-2
# 3-2
# 4-1

def id_count(id_num):
    my_list = []
    
    for i in range(0,10):
        my_list.append(0)
    
    while(id_num > 0):
        current_digit = id_num % 10
        current_count = my_list[current_digit] + 1          #my_list[4] + 1 = 1
        my_list[current_digit] = current_count              # [0,0,0,0,1,0,0,0,0,0,0]
        id_num = id_num//10                                 # 1122334 // 10 = 112233
        print(my_list)
        
    for i in range(len(my_list)):
        print(f"{i} - {my_list[i]}")
        
print(id_count(11223))

    