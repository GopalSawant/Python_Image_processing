class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


catObj1 = Cat("Tom", 16)
catObj2 = Cat("Mini", 2)
catObj3 = Cat("Ini", 5)


def oldestcat(*args):
    return max(args)


print(f'The oldest cat is {oldestcat(catObj1.age,catObj2.age,catObj3.age)} year old')
print(Cat.species)