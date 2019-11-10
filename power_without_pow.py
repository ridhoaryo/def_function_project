def pangkat(x, y):
    hasil_pangkat = x
    for i in range(y-1):
        hasil_pangkat *= x
    return hasil_pangkat

print(pangkat(6,5))
print('confirm {0}'.format(pow(6,5)))