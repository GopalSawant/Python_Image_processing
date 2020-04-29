def my__decorator(func):
    def any_fun(*args):
        print("*************")
        func(*args)
        print("*************")

    return any_fun


@my__decorator
def hello(*args):
    print("helloooo")
    print(*args)


hello('Hi!!!!!!!!!!')
