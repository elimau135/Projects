class WordReverser:
    
    user_input = str(input('Please provide a word that should be reversed: '))
    
    wordList = list(user_input)
    attr_len = len(wordList)
    
    reversedWordlist = []
    word = type(str)
    
    for i in range(attr_len, 0, -1):
        index = i-1
        word = wordList[index]
        reversedWordlist.extend(word)
        i-1
    
    i = 0
    while i <= attr_len:
        if i == attr_len:
            print(''.join(map(str, reversedWordlist)))
        i +=1    