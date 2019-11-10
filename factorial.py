def factorial(x):
    angka = 1
    if x == 1:
        return x
    elif x == 0:
        return x+1
    elif x < 0:
        return 'Not definied'
    else:
        for i in range(1, x+1):
            angka *= i
    return angka

print(factorial(4))