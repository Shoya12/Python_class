"""
Loop:
    For : when we know no of interation/no. of repetiiton 
    While: 
"""
# course='python'
# for i in course:
#      print(i)


# To print from 10 to 0 . 
# for i in range(10,0,-1):
#     print(i)

"""
While Loop : 
 
syntax :
while cond :
statment

"""
# i=0 
# while i<5:
#     print(i)
#     i=i+1
# print('pokahara')

# password=input('Enter your password')
# while password!='password123':
#     break
# print('You entered our system')
       
# ******'Break' in control loop '*****
# i=1 
# while True :
#     print(i)
#     i=i+1
#     if i==5:
#         break
# print('Your value for i has reached 5 ')

# ******'Continue' in control loop ' ****
i=0
while True:
    i=i+1
    if i==5:
     print(i)
     continue 
    elif i==8:
        break
print(i)
