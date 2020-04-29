import random


def user_number_validation(number):
    while number > 10 or number < 1:
        number = int(input("Please Enter integer number between 1 to 10: "))
    return number


while True:
    user_number = int(input("Enter integer number between 1 to 10: "))
    user_number_validation(user_number)
    system_number = random.randint(1, 10)
    if system_number == user_number:
        break

print(f'Bingoooooooooooooo you won; your number matches system random number')

# user_number = int(input("Enter integer number between 1 to 10: "))
# user_number_validation(user_number)
# system_number = random.randint(1, 10)
#
# while system_number != user_number:
#     print(f'Oops your number is {user_number} and system number is  {system_number}')
#     user_number = int(input("Enter integer number between 1 to 10: "))
#     user_number_validation(user_number)
#     system_number = random.randint(1, 10)
#
# print(f'Bingoooooooooooooo you won your number matches system random number')
