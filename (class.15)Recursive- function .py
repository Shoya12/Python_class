"""
Recursive Function : a function calling itself 

"""
# *** Example or recursive function *** #

def count(n):
    if n==0:  # base case/exit condition 
        return 
    print(n)
    count(n-1)  # recursive case 
count(5)

def factorial(n):
    if n==1:
        return 1 
    else:
        return n*factorial(n-1)

print(factorial(4))