"""
Function 

def function_name():  # declaration 
    block of code 
function_name().     # calling 


"""
# Examples-

# def name_taker():
#     name=str(input('Enter your name'))
#     print(name)
# name_taker()

# def sum():
#     a=float(input('Enter a number'))
#     b=float(input('Enter another number'))
#     print('sum=',a+b)
# sum()

#  Parameter and Argument
#  def add(a,b)
    # print(a+b)
#  add (2,5)

# def even_odd_check(x):
#    if x %2==0:
#       return f'{x} is even'
#    else:
#       return f'{x} is odd number '
# print(even_odd_check(9))

# Default Parameter
# def show_details(name,age,country='Nepal'):
#     print(f'Hello my name is{name}.I am {age} yrs old.I am from {country}')
# show_details('Ram',25,'India')

"""
Types of argument: - Positional Argument(spefic argument in specific postion gives specific value to parameter)
                   - Keyword Argument: 
                def show_details(name,age,country='Nepal'):
                print(f'Hello my name is{name}.I am {age} yrs old.I am from {country}')
                show_details(name='Ram',age=25,country='India')
"""
# def problem():
#     def square_num():
#         n=input('')
#         sq=int(n)**2
#         return sq
#     result1=square_num()
#     def cube_num():
#         no=input('')
#         cb=no**3 
#         return cb 
#     result=cube_num()
#     print(result1)
#     print(result)
# problem()

#  note :If you use 'return' , even if you call the function with an argument nothing is printed , so a variable is kept equal to an function name and it is printed .
# def sum (a,b=7):
#     return a+b 
# result=sum(5)
# result1=sum(5,8)
# print(result)
# print(result1)
