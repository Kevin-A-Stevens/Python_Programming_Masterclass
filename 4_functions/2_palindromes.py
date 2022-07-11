"""
A palindrome is a word that reads the same
backwards and forwards

"""


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()
    # returns True/False


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))





