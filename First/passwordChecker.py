#Password Checker

username=input('Please enter the username ')
password=input("Please enter the password ")

pwd=('*' * len(username))
print(f"Hey {username}, your password {pwd} is {len(password)} letters long")
