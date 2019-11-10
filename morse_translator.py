def morse_translator(morse):
    morse_dict = {
        'a': '._',
        'b': '_...',
        'c': '_._.',
        'd': '_..',
        'e': '.',
        'f': '.._.',
        'g': '__.',
        'h': '....',
        'i': '..',
        'j': '.___',
        'k': '_._',
        'l': '._..',
        'm': '__',
        'n': '_.',
        'o': '___',
        'p': '.__.',
        'q': '__._',
        'r': '._.',
        's': '...',
        't': '_',
        'u': '.._',
        'v': '.._',
        'w': '.__',
        'x': '_.._',
        'y': '_.__',
        'z': '__..',
        ' ': '/'
    }
    morse_code = morse
    if morse_code.isalpha():
        morse_translate = ''
        for c in morse_code:
            if c in morse_dict.keys():
                morse_translate += morse_dict[c]
        return morse_translate
    else:
        morse_translate = []
        morse_list = morse_code.split(' ')
        for code in morse_list:
            for c, m in morse_dict.items():
                if code == m:
                    morse_translate.append(c)
        translate = ''.join(morse_translate)
        return translate

words = input('insert words (separate each morse with space if you want translate morse to alphabet): ')
result_morse = morse_translator(words)
print(f'Kata dari sandi morse "{words.upper()}" adalah "{result_morse}"')