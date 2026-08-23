"""
**always start with backslash- \n 
**for space of four character -\t 


"""

a='Hello'
b='World'
print(a+b)

print(a+'\n' +b)
print(a+'\t'+b)

print('Hello \nWorld')
print('Hello \tWorld')

# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."

# The escape character allows you to use double quotes when you normally would not be allowed:
# txt = "We are the so-called \"Vikings\" from the north."