## DATA TYPES IN PYTHON ##
# 1)Numeric Data Types < Integer , Float 
# 2)String Data Type 

#####Type Casting in Python #####
# 1) Implicit Type Casting
# 2) Explicit Type Casting

#1) Implicit Type Casting 
 
#e.g:1 
"""

x=17 
print(type(x))
p=str(x)
print(type(p))

"""


#e.g:2
"""
variable1='678'
print(type(variable1))
print(type(int(variable1)))

"""

#Homework: Convert 10.8 in integer , string and boolean data type and print the type of each variable

y=-10.8
print(type(y))

i=int(y)
print(i)
print(type(i))

s=str(y)
print(s)
print(type(s))

b=bool(y)
print(b)
print(type(b))



# print('Welcome to the plaza')
# answer=input('What is the word for the place you are in ?')
# y=answer.upper()
# if 'H' in y:
#     print(len(answer))
#     x=answer[0]
#     print('Here is your validation ', x)
#     r=answer.replace('H','J')
#     print(r)