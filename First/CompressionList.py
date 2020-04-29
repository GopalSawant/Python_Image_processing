my_list = []

print(list(number for number in range(100)))
print(list(number for number in range(100) if number % 2 == 0))
print(list(number for number in range(1, 100, 2)))

set1 = {number ** 2 for number in range(100) if number % 2 == 0}
print(sorted(set1))

my_dictionary = {
    ''
}

print({k: k ** 2 for k in [1, 2, 3]})
