# Write a function called first_diff that is given two strings and returns the first location in which the strings differ. 
# If the strings are identical, it should return -1.

def first_diff(string1,string2):
  len1 = len(string1)
  len2 = len(string2)
  len_ = min(len1, len2)
  
  for i in range(len_):
    if string1[i] != string2[i]:
      return i
      
  if len1 == len2:
    return -1


print(first_diff('book','rise'))