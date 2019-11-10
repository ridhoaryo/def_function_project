def pangkat3(x, y):
    if y == 1:
        return x
    else:
        return x * pangkat3(x, y-1)

print(pangkat3(2,3))