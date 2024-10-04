word = input("Введите слово: ")
wordLen = len(word)
middleCharacter = wordLen // 2

if(len(word) % 2 != 0):
    print(word[middleCharacter])
else:
    print(word[middleCharacter-1:middleCharacter+1])