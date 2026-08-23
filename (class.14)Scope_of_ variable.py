"""
Scope of variable :< Local Variable
                  :<Global Variable 
                  :<Enclosing Variable 
"""
name='ram' # global variable 
def show_details():
    x=7 #local variable 
    print(f'My name is {name}')
    return x 

    # print(x)
b=show_details()
print(b)

# Enclosing Variable:

# def outer():
#     name='Hari'
#     def inner():
#         print(name)
#     inner()
# outer()

    