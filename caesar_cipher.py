def caesar_cipher(word):
    abjad = list('abcdefghijklmnopqrstuvwxyz')
    kata_caesar = word.lower()
    caesar_cipher_word = ''
    for c in kata_caesar:
        index = (abjad.index(c) + (2%len(abjad)))%len(abjad)
        caesar_cipher_word += abjad[index]
    return caesar_cipher_word

kata_kata = input('masukkan kata: ')
result_caesar = caesar_cipher(kata_kata)
print(f'bentuk Caesar Cipher dari kata "{kata_kata.upper()}" adalah "{result_caesar.upper()}"')