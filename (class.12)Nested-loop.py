for i in range(5):
    for j in range(4):
     print('*')

for i in range(3):
   for j in range(3):
      print(i,j)


for i in range(4):
   for j in range(3):
      print(i,j)

# If we need to print a certai n pattern.
# We need to identify a certain pattern , where the outer function is equal to no of rows and j=i+1 

# *
# **
# ***
# **** 

for i in range(4):
   for j in range(i+1):
      print('*',end='')
   print('')

# Another patten just like above but in right alignment 

# *****
#  ****
#   ***
#    **
#     *



   
