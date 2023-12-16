data = [
    {'name':'Kwadwo', 'phone':'555-1414', 'email':'kwadwo@mail.net'},
    {'name':'Daniel', 'phone':'555-1618', 'email':'daniel@mail.net'}, 
    {'name':'Akwasi', 'phone':'555-3141', 'email':''}, 
    {'name':'Andy', 'phone':'555-2718', 'email':'andy@mail.net'}
]
# (a) All the users whose phone number ends in an 8

for item in data:
    for value in item.values():
        if value.endswith("8"):
            print(item)


# (b) All the users that don’t have an email address listed
print("\n")
for item in data:
    for value in item.values():
        if value == '':
            print(item)