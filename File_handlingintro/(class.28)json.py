"""
json : javascript object notation , data format 

"""

"""
import json 
student ={
        'id':11,
        'name':'Ram'
    }

print(type(student))

json_formatted_data = json.dumps(student)
print(type(json_formatted_data))
print('\n')

print(type(json_formatted_data))

"""

#writing json data to jsonfile.json 
"""
import json 
student ={
        'id':11,
        'name':'Ram'
    }
with open('/Users/acharya_shobhaya/Desktop/Learn_Python/File_handlingintro/(class.28)jsonfile.json','w') as file:
    json.dump(student,file)
"""

# reading json data from jsonfile.json using load() method . 

"""
import json
with open('/Users/acharya_shobhaya/Desktop/Learn_Python/File_handlingintro/(class.28)jsonfile.json','r') as file:
    data=json.load(file)
    print(data)
"""

# updating json data from jsonfile.json and wrting it back to the same file using dump() method.

"""
import json
student={
    'id':11,
    'name':'Ram'
   }
with open('/Users/acharya_shobhaya/Desktop/Learn_Python/File_handlingintro/(class.28)jsonfile.json','r') as file:
    data=json.load(file)

data['id']=12
data['name']='Shyam'

with open('/Users/acharya_shobhaya/Desktop/Learn_Python/File_handlingintro/(class.28)jsonfile.json','w') as file:
    json.dump(data,file)

"""