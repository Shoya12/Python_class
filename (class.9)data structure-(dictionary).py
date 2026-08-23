"""
Dictionary: kept in key value pair, {key:value}
syntax :{}

"""
car={ 
    'brand':'Toyota',
    'color':'Red',
    'price':8000

}
# print(type(car))
print(car)

# Creating empty dictionary 
# new_car={}

# Getting specific value from specfic keys 

print(car['brand'])
print(car.get('price'))

# Prints all the keys 
print(car.keys())

# Prints all the values 
print (car.values())

# Updating values of specific keys 
car['brand']='Tesla'
car['color']=['red','pink']
print(car)

# Adding a completely new key & value 
car['model']=2026
car.update({'engine type':'electric'})
print(car)

# Loop in a dicitonary 

for i in car:
    print(i)


for i,j in car.items():
    print(i,j)


# Nested Dictionary 

car={ 
    'car1':{
    'brand':'Toyota',
    'color':'Red',
    'price':8000
    },

    'car2':{
    'brand':'Tesla',
    'color':'Red',
    'price':85000
    
    }
}
print(car['car1'])
print(car['car2']['price'])
