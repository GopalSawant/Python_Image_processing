from DecoratorPerformanceTest import performance_test
from PackageTest.PackageFileTest import your_name

print(__name__)

@performance_test
def fibo_genearator(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = b
        b = a + b
        a = temp


@performance_test
def fibo_list(number):
    a = 0
    b = 1
    for i in range(number):
        # print(a)
        temp = b
        b = a + b
        a = temp


print(your_name('Gopal'))
fibo_genearator(10000)
fibo_list(10000)
