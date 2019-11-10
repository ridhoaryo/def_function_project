def basic_calc(num_1, ops, num_2):
    if str(ops)=='+':
        return sum(num_1, num_2)
    elif str(ops)=='-':
        return num_1-num_2
    elif str(ops)=='/':
        return num_1/num_2
    elif str(ops)=='*':
        return num_1*num_2

hasil = basic_calc(float(input('input first number: ')), input('input math operation: '), float(input('input second number: ')))
print(hasil)