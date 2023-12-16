"""
Write a class called Password_manager.

The class should have a list called old_passwords 
that holds all of the user's past passwords.

The last item of the list is the user's current 
password.

There should be
A method called get_password that returns the current password 
A method called set_password that sets the user's password.

The set_password method should only change the 
password if the attempted password is different
from all the user's past passwords.

Finally, create a method called is_correct that
receives a string and returns a boolean True or 
False depending on whether the string is equal
to the current password or not.
"""

# class PasswordManager():
#     old_passwords = []

#     def set_password(self, new_password):
#         if new_password not in self.old_passwords:
#             self.old_passwords.append(new_password)
#             return new_password
#         else:
#             return "Password already used. Try a new one"

#     def get_password(self):
#         return self.old_passwords[-1]

#     def is_correct(self, check_password):
#         if check_password == self.get_password():
#             return True
#         else:
#             return False

# pwd = PasswordManager()

