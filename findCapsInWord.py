def capital_letters(word: str):
    Caps = []
    for i in word:
        if i.isupper():
            Caps.append(i)
    return Caps

def capital_indexes(word: str):
    indexes = []
    for i in range(len(word)):
        if word[i].isupper():
            indexes.append(i)
    return indexes

word = input('Please type a word: ')

Caps = capital_letters(word)

indexes = capital_indexes(word)

print(' The capital letters are + ', Caps, 'and they are located at ',indexes)