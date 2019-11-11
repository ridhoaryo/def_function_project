romanDict = {
    'M' : 1000,
    'CM': 900,
    'D' : 500,
    'CD': 400,
    'C' : 100,
    'XC': 90,
    'L' : 50,
    'XL': 40,
    'X' : 10,
    'IX': 9,
    'V' : 5,
    'IV': 4,
    'I' : 1
}

def romanNum(param):
    newString = ''
    while param >= 1:
        for i in list(romanDict.values()):
            how_many = int(param/i)
            roman_keys = list(romanDict.keys())
            roman_values = list(romanDict.values())
            
            newString += how_many * roman_keys[roman_values.index(i)]
            param = param % i
    
    print(newString)

romanNum(int(input('Masukkan angka : ')))