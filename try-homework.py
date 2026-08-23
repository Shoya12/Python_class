
i=1
total_sum=0
value=0
number_after=0
sum=0
until_list=[]
while i>=1:
    j=int(input('Enter sequence of integer value'))
    i=i+1
    until_list.append(j)
    print(until_list)
    if 27 in until_list:
     value=until_list.index(27)
     number_after=until_list[value+1:]
    total_sum=sum(number_after)
    if 0 in until_list:
       break
print(f'Sum is {total_sum}')
    
   
#  print(value)
# continue 
# if j==27:
#     for h in j:
#       if h>=27:
#        sum=sum+1
#     if h==0:
#       break
# print(f'Sum of values is (sum)')
