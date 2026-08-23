"""
Mini Student Managment System 

"""


student_detail_list=[]
subject=('Science','Math','English','Nepali','Social')

# student_detail_list=[{'id':1,'name':'ram','marks':[77,44,56,78,89]},{'id':5,'name':'shyam','marks':98}]

while True:

    print('1.Add Student\n 2.View Student \n 3.Passsed \n 4.Failed \n 5.Remove Student \n 6.Exit')
    choice=int(input('Enter your choice from 1 to 6 '))
    if choice <1 or choice >6:
       print('Invalid choice')
       continue 

    match choice:
     
        case 1:
            # id=int(input('Enter the student id:'))
            # name=input('Enter the student name: ')
            # marks=float(input('Enter the marks of the student: '))

            # studentadd={
            # 'id':id,
            # 'name':name,
            # 'marks':marks
            # }
            # student_details.append(studentadd)
            # print('The student is added successfully')
           id=int(input('Enter the student id:'))
           if id in student_detail_list:
              print('Student already exists')
              continue
           else :
              name=input('Enter your name')
              mark_list=[]
              for i in subject:
                 mark=float(input(f'Enter the marks for your {i}:'))
                 mark_list.append(mark)

              student_dict={
                  'id':id,
                  'name':name,
                  'marks':mark_list
               }
              student_detail_list.append(student_dict)
              print('The student was added succesfully')
           


              
        case 2:
             print('ID\tName\tMark')

             for i in student_detail_list:
               print(f"{i['id']}\t{i['name']}\t{i['marks']}")

        case 3:
         #  pass_count=0
         #  for i in student_detail_list:
         #     if i['marks']>40:
         #        print(i['name'])
         #        pass_count=pass_count+1
         #  print(f'The total number of student passed is :{pass_count}')
         total_passed_student=0
         p=0
         for i in student_detail_list:
            for j in i['marks']:
               if j>=40: 
                  p=p+1
            
            if p==5:
                 print(i['name'])
                 total_passed_student+=1
         print(f'The toal passed student is {total_passed_student}')

        case 4:
         # fail_count=0
         # for i in student_detail:
         #        for j in mark:
         #           sum=0

         #        if i['marks']<40:
         #         print(i['name'])
         #         fail_count=fail_count+1
         # print(f'The total number of student failed is :{fail_count}')
         total_failed_student=0
         failed=0
         for i in student_detail_list:
            for h in i['marks']:
               if h<=40:
                  failed=failed+1
            if failed>=1:
                  print(i['name'])
                  total_failed_student+=1
         print(f'Total no of student failed are: {total_failed_student}')






        case 5:
            remove_id=int(input('Enter the id of the student to be removed'))
            for i in student_detail_list :
               if i['id']==remove_id:
                  student_detail_list.remove(i)
            print('Succesfully removed')
               

        case 6:
         print('Thank you for using student managment system')
         break 





