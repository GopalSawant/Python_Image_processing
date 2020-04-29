#Formated String
name="Gopal"
age=25
address="Pune"
print(f'Hi {name}. you are {age} and you live {address}, right? ')
print('Hi {}. you are {} and you live in {}'.format(name,age,address))
print('Hi {}. you are {} and you live in {}'.format(name,55,address))
print('Hi {2}. you are {1} and you live in {0}'.format(name,age,address))

info='Hi Gopal. you are 25 and you live in Pune'
print(info[6])
print(info[:])
print(info[0:2])
info='0123456789'
print(info[0::2])
print(info[-7:-1:2])

