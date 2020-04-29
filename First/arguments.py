 #*args **kwargs
def sumOfArguments(*args, **kwargs):
    print(kwargs)
    return sum(args)+sum(kwargs.values())


print(sumOfArguments(1,2,3,4,5,6,7,8,9, num1=45 , num2=10))
