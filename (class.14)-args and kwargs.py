"""
Args and Kwargs 

Args : use args to receive multiple positional argument with simgle single parameter 

"""

# *************Ex of Args.( for postional argument)********:

# def show_detail(*data):
#     for i in data:
#         print(i)
# show_detail('ram',78,'nepal')

# In the above example multiple argument are passed just to a single argument , before me needed multipe 
# multiple parameter to store multiple argument 

# ************* Kwargs (for keyword argument)************************
""" 

def show_detail(**data):
   print(f'My name is {data['name']},I am {data['age']}')
show_detail(name='ram',age=78,country='nepal')

"""

# *********** Lambda function ********* 
"""
Lambda function is an anonymous fucntion that contains small line of code:
>> Contains the keyword :lambda 

syntax : lambda variable : expression/logic 
"""
# Simple example 
# add=lambda x: x+10
# print(add(10))

# function=lambda x,y :x+y 
# result=function(3,5)
# print(result)

