"""
csv : comma separated values , data format

-excel stores data in csv format 

for example:ID,Name,Age 
            1,'Hari',66
            7,'Laxmi',32

"""

# writing csv data to csvfile.csv using writerow() method.
"""
import csv 
with open('/Users/acharya_shobhaya/Desktop/Learn_Python/File_handlingintro/csvfile.csv','w') as file:
    writer=csv.writer(file)

    writer.writerow(['ID','Name','Age'])
    writer.writerow([1,'Hari','66'])
    writer.writerow([7,'Laxmi',32])
"""

# reading csv data from csvfile.csv using reader() method.
"""
import csv

with open('/Users/acharya_shobhaya/Desktop/Learn_Python/File_handlingintro/csvfile.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
"""

# Creating a new csv file and writing data to it using DictWriter() method.(USING DICTIONARY)
""" 
import csv 
with open('/Users/acharya_shobhaya/Desktop/Learn_Python/File_handlingintro/csvfile.csv','w',newline='') as file:
    fieldname=['ID','Name','Age']

    writer=csv.DictWriter(file,fieldnames=fieldname)

    writer.writeheader()
    writer.writerow({
        'ID':1,
        'Name':'Ram',
        'Age':67
    })
    writer.writerow({
        'ID':2,
        'Name':'Shyam',
        'Age':32
    })
"""