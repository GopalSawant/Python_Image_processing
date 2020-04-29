class SimpleClass:
    x = 5
    classAge = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'Your name and age is {self.name}, {self.age}')

    def newDisplay(self):
        print("Hello")


# simpleObj = SimpleClass()
simpleObj1 = SimpleClass('Gopal', 25)
print(simpleObj1.x)
# simpleObj1.age=40
print(simpleObj1.age)
print(simpleObj1.classAge)
simpleObj1.display()
simpleObj1.newDisplay()
del simpleObj1.age
del SimpleClass.classAge

# simpleObj1.newDisplay()
