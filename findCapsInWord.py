def capital_indexes(word: str):
    myList = []
    for i in word:
        if i.isupper():
            myList.append(i)
    return myList

word = input('Please type a word: ')

Caps = capital_indexes(word)

print(Caps)