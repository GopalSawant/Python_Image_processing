class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"Animal {self.name} is walking around"
    # return


class Simon(Cat):
    def sing(self, sound):
        return f'{sound}'


class Sally(Cat):
    def sing(self, sound):
        return f'{sound}'


class Mini(Cat):
    def sing(self, sound):
        return f'{sound}'


simon_obj = Simon("simon", 1)
sally_obj = Sally("sally", 2)
mini_obj = Mini("mini", 3)

print(Mini.mro())

my_cat = [simon_obj, sally_obj, mini_obj]

petclass_obj = Pets(my_cat)

petclass_obj.walk()
