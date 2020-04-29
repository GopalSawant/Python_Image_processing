from time import time


def performance_test(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        print(f"This function took {end_time - start_time}s")

    return wrapper

#
# @performance_test
# def multiplication():
#     for number in range(100000000):
#         number * 5
#
#
# multiplication()
