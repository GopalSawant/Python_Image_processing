# Functional programming
# data and functions separations
# Map Function


def multiply_by2(item):
    return item * 2


my_list = [1, 2, 3]
print(list(map(multiply_by2, my_list)))


def addition(my_list):
    pass


print(list(map(addition, my_list)))
