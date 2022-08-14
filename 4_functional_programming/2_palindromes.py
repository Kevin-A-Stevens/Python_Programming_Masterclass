"""
A palindrome is a word that reads the same
backwards and forwards

functions used
print()
input()

methods used
.isalnum()
.casefold()
"""


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()
    # returns True/False


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return is_palindrome(string)


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))




