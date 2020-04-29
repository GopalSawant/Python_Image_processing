my_list = ['a', 'b', 'c', 'd', 'a', 'c']
duplicate_list = []

duplicate_list = list(set([item for item in my_list if my_list.count(item) > 1]))
print(duplicate_list)