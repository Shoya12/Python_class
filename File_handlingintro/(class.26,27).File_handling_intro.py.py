"""
File Handling :create ,read ,write ,delete 

modes-

read :r mode 
write : w mode 
append : a mode 
create: x mode 
"""

# Opening a file in write mode and writing to it.

# f = open('/Users/acharya_shobhaya/Desktop/Learn_Python/File_handling_py_intro.py/new_file.txt', 'w')
# f.write('Hello World')
# f.close()

# Opening a file using 'with open' 
"""
with open('/Users/acharya_shobhaya/Desktop/Learn_Python/File_handling_py_intro.py/new_file.txt', 'a') as file:
    file.write('You are right')

"""
# Using os module to rename a file and create another folder respectively 

"""
import os
os.rename('new_file_for_filehandling.txt', 'new_file.txt')

os.mkdir('new_folder')

"""

#Deleting a folder using os module

"""
import os
os.rmdir('new_folder')
"""
