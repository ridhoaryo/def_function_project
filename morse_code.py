def morse_translator(word):
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
    kata_morse = word.lower()
    morse_translate = ''
    for c in kata_morse:
        if c in morse_dict.keys():
            morse_translate += morse_dict[c]+' '
    return morse_translate

words = input('insert words: ')
result_morse = morse_translator(words)
print(f'Sandi morse dari kata "{words.upper()}" adalah {result_morse}')