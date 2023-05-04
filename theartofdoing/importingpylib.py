
'''
import random #this imports the library random from py libraries
for i in range(10):
    print(random.randint(1,1000))

#This program will print random no. from 1 to 1000

'''

import subprocess
output = subprocess.check_output('ls',shell=True)
print(output)

#This program output all files and folders where it is located.

output = subprocess.check_output('pwd',shell=True) #this show the dir you are
print(output)

