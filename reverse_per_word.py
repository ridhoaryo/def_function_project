def reverse_words(word):
    sentence = word
    sent_list = sentence.split()
    sent_rev_list = []
    for word in sent_list:
        sent_rev_list.append(word[::-1])
    sent_rev = ' '.join(sent_rev_list)
    return sent_rev
    
print(reverse_words(input('masukkan kalimat: ')))