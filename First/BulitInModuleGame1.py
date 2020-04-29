import random


def luck_check(user_number, system_number):
    if 11 > user_number > 0:
        if user_number == system_number:
            print("Congratulations")
            return True
    else:
        print("Please enter number between 1-10")


system_number = random.randint(1, 10)
while True:
    try:
        user_number = int(input("Enter number between 1-10: "))
        if luck_check(user_number, system_number):
            break

    except ValueError as err:
        print("Please enter  a integer number ")
        continue
