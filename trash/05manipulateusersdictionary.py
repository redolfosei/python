data = [
        {'name':'Kwadwo', 'phone':'555-1414', 'email':'kwadwo@mail.net'},
       {'name':'Daniel', 'phone':'555-1618', 'email':'daniel@mail.net'}, 
       {'name':'Akwasi', 'phone':'555-3141', 'email':''}, 
       {'name':'Andy', 'phone':'555-2718', 'email':'andy@mail.net'}
]
       
# (a) All the users whose phone number ends in an 8
for key in data:
  p = key['phone']
  if p[-1] == '8':
    print(f"This user phone number ends with 8: {key}")
  
# (b) All the users that don’t have an email address listed
for key in data:
  email = key['email']
  if email == '':
    print(f"{key} has no EMAIL")
    
    
  