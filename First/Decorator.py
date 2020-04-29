class Sum:

    @staticmethod
    def addition(num1, num2):
        return num1 * num2

    @classmethod
    def addition(cls, num1, num2):
        cls.num1 = num1
        cls.num2 = num2
        return num1 + num2


print(Sum.addition(2, 3))
object1 = Sum()
print(object1.addition(10, 10))
