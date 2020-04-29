from functools import reduce

# 1 Capitalize all of the pet names and print the list
# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# 3 Filter the scores that pass over 50%

my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalisation(item):
    return item.upper()


my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
my_numbers.sort()
print(my_numbers)

scores = [73, 20, 65, 19, 76, 100, 88]


def score(score_number):
    return score_number > 50


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(list(map(capitalisation, my_pets)))
print(list(zip(my_strings, my_numbers)))
print(list(filter(score, scores)))


def accumelator(acc, item):
    return acc + item


print(reduce(accumelator, (my_numbers + scores)))
