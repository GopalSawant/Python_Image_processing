try:
    with open('C:\\Users\Vaishali Sawant\Desktop\Simple\simple.txt', mode='r+') as my_file:
        my_file.write("hey don\'t be happy we are gonna delete you anyways")
        my_file.seek(0)
        print(my_file.readlines())
except FileNotFoundError:
    print("File not found")
