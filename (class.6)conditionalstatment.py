# num=int(input('Enter any number'))
# if num%2==0:
#     print('It is an even number')
# else:
#     print('It is an odd number')


marks=float(input('Enter your marks'))
if marks <=0 and marks >100:
        print('Invalid Marks')
elif marks>=90 and marks<=100:
        print('You got A+ grade')
elif marks>=80 and marks<90:
        print('You got A grade')
elif marks>=70 and marks<80:
        print('You got B grade')
elif marks>=60 and marks<70:
        print('You got C grade')
elif marks>=50 and marks<60:
        print('You got D grade')
elif marks>=40 and marks<50:
        print('You got E grade')
else:
        print('Sorry ! Try next time')
choice=str(input('Do you want to enter your marks again'))



# Nested conditional statment (loop inside a loop )
"""
num=int(input('Enter any number'))
if num>0:
        if num%2==0:
                print('It is an even no.')
        else:
                print('It is odd no.')
else:
        print('The no. should be greater than zero')
"""
