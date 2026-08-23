
print('1.Addition\n 2.Subtraction\n 3.Divison \n 4.Multiplication \n 5.Exit')
while True :
    choice=int(input('Enter your choice'))
    if choice <0 or choice >5:
     print('Invalid choice')
     continue 
    elif choice==1:
        num_1=float(input('Enter the first number'))
        num_2=float(input('Enter the second number'))
        result=num_1+num_2
        print(f'The sum of {num_1} and {num_2}  is {result}')

    elif choice==2:
        num_1=float(input('Enter the first number'))
        num_2=float(input('Enter the second number'))
        result=num_1-num_2
        print(f'The difference between{num_1} and {num_2} is {result}')

    elif choice==3:
        num_1=float(input('Enter the first number'))
        num_2=float(input('Enter the second number'))
        result=num_1//num_2
        print(f'The divison between{num_1} and {num_2} is {result}')

    elif choice==4:
        num_1=float(input('Enter the first number'))
        num_2=float(input('Enter the second number'))
        result=num_1*num_2
        print(f'The product between{num_1} and {num_2} is {result}')

    elif choice==5:
        print('Thank you')
        break

        
    
    
     
     