# with open('Test.txt', mode='r') as my_file:
#     print(my_file.readline())
#     my_file.seek(0)
#     print(my_file.readline())

# with open('Test.txt', mode='r+') as my_file:
#     # print(my_file.readlines())
#     my_file.writelines('yess dude it\'s me again, and i see you can do it ')
#     my_file.seek(0)
#     print(my_file.readlines())


with open('Test.txt', mode='a') as my_file:
    my_file.write("\n")
    my_file.writelines('yours sincerely')

with open('Test.txt', mode='r') as my_file:
    print(my_file.readlines())

with open('NewTest.txt',mode='w') as new_file:
    new_file.write("helooo")
