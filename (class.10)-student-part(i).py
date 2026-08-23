"""
Mini Student Managment System 

"""
student_details=[]
# student_detail=[{'id':1,'name':'ram','marks':77},{'id':5,'name':'shyam','marks':98}]

while True:

    print('1.Add Student\n 2.View Student \n 3.Passsed \n 4.Failed \n 5.Remove Student \n 6.Exit')
    choice=int(input('Enter your choice from 1 to 6 '))

    match choice:
     
        case 1:
            id=int(input('Enter the student id:'))
            name=input('Enter the student name: ')
            marks=float(input('Enter the marks of the student: '))

            studentadd={
            'id':id,
            'name':name,
            'marks':marks
            }
            student_details.append(studentadd)
            print('The student is added successfully')
    
        case 2:
             print('ID\tName\tMark')

             for i in student_details:
              print(f"{i['id']}\t{i['name']}\t{i['marks']}")

        case 3:
          pass_count=0
          for i in student_details:
             if i['marks']>40:
                print(i['name'])
                pass_count=pass_count+1
          print(f'The total number of student passed is :{pass_count}')

        case 4:
         fail_count=0
         for i in student_details:
                if i['marks']<40:
                 print(i['name'])
                 fail_count=fail_count+1
         print(f'The total number of student failed is :{fail_count}')
         

        case 5:
            remove_id=int(input('Enter the id of the student to be removed'))
            for i in student_details:
               if i['id']==remove_id:
                  student_details.remove(i)
                  print('Succesfully removed')
               

        case 6:
         print('Thank you for using student managment system')
         break 





