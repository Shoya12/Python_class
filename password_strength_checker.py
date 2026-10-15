
print("=== PASSWORD STRENGTH CHECKER ===")
password = input("Enter your password to check its strength: ")

length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():  
        has_special = True

score = 0
if length >= 8:
    score = score + 1
if has_upper:
    score = score + 1
if has_lower:
    score = score + 1
if has_digit:
    score = score + 1
if has_special:
    score = score + 1

if score == 5:
    print("Result: STRONG PASSWORD!")
elif score >= 3:
    print("Result: MODERATE PASSWORD ")
else:
    print("Result: WEAK PASSWORD!")