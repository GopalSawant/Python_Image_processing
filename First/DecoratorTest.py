# '''Higher order function is a function which
# either accepts the function as parameter or return the function for example MAP
# or
# def anyFunction(function1):
#     do some operation
# '''


def any_function(function1):
    print(f"what were you expecting")
    return function1()

    # print(f"what will function return to you {return1} ")


def some_other_function():
    print( f"what were you expecting")
    # return 2 + 3


# any_function(some_other_function)

@any_function
def hello():
    print("helooooooo")
