from time import time



# Decorator
def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        print(f'The function took {end_time - start_time}')
        print(__name__)

    return wrapper


@performance
def number_multiplication(num):
    empty_list = []
    for number in range(num):
        empty_list.append(number * 5)
    return empty_list


@performance
def generator_function(number):
    for number in range(number):
        yield number*5


number_multiplication(10000000)
generator_function(10000000)

# g=generator_function(1)
# print(next(g))
# multi_list=number_multiplication(1000)
# print(multi_list)
#
# print(generator_function(10000))
