'''
numbers = [1,2,3,4,5,6,7,8,9,10]
new_list = [n + 1 for n in numbers]
print("New List is {0} ".format(new_list))
'''

'''
name = "Redolf"
new_name = [letter for letter in name]
print(new_name)
'''

# second_range = [number * 2 for number in range(1,5)]
# print(second_range)

names = ["Redolf","Sam","Osei","Ama","Optis","Daniel","Kesse"]
short_name = [name for name in names if len(name) < 5]
print(short_name)
long_name_upper_casse = [uname.upper() for uname in names if len(uname) >= 5]
print(long_name_upper_casse)






