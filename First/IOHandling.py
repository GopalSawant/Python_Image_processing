# my_file=open('C:\\Users\\Vaishali Sawant\\esktop\\PYTHON\\PyCharm\\First\\Test.txt')
my_file = open('Test.txt')

# print(my_file)
print(my_file.read(50))
my_file.seek(0)
print(my_file.readline())
print(my_file.readlines())

my_file.close()
my_file.readline()
