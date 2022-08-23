def isPalindrome (word):
    #solution 1
        word = word.lower().replace(' ', '')
        return word == word[::-1]

print(isPalindrome("Malam"))

