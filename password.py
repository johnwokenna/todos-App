password = input("Enter password: ")
password_check = {}

if len(password) >= 8:
    password_check['length'] = True
else:
    password_check['length'] = False

check_digit = False
for char in password:
    if char.isdigit():
        check_digit = True
password_check['digit'] = check_digit

check_upper = False
for char in password:
    if char.isupper():
        check_upper = True
password_check['upper'] = check_upper

print(password_check)

if all(password_check.values()):
    print("Strong password")
else:
    print("Weak password")