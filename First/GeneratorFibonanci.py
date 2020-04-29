# def fib_series(number):
term, next_term = 0, 1
my_list = list(range(21))
if not my_list:
    print("please enter positive integer ")
elif my_list == [0]:
    print("1")
else:

    for number in my_list:
        print(term)
        sum_term = term + next_term
        term = next_term
        next_term = sum_term



# def fibo(number):
#     a = 0
#     b = 1
#     for i in range(number):
#         yield a
#         temp = b
#         b = a + b
#         a = temp
#
# fibo(100)