def isPalindrom(word):
    word = word.lower()
    return word == word[::-1]

s = str(input())    
print(isPalindrom(s))