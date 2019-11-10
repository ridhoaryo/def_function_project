def factorial(x):
    if x == 1:
        return x
    elif x == 0:
        return x+1
    elif x < 0:
        return 'Not definied'
    else:
        return x * factorial(x-1)

print(factorial(5))