class User:

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


class Wizard(User):

    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power
        self.email = email

    def attack(self):
        print(f"the {self.name} in action has {self.power} power and has email id {self.email}")


class Archer(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"The {self.name} is archer and has {self.arrows} arrows")


wizard1 = Wizard("krishna", 10000, "gopal@gmail.com")
wizard1.sign_in()

archer1 = Archer("Arjun", 1000, "archer@gmail.com")

wizard1.attack()
archer1.attack()
