def odd_even(x):
    if x%2 == 0:
        print('{} is an even number!'.format(x))
    else:
        print('{} is an odd number!'.format(x))

odd_even(float(input('Input number: ')))