"""
function annotations
give a way to describe our functions without
referring to the docstring

def function_name(parameter: data_type) -> return_type:

function annotations make it clear what data types
they accept and what they return

use annotations as well as docstrings
to have clearly notated functions

check banner.py for how to annotate default parameters

Also check banner.py on how to add raise errors
in a docstring
"""


def multiply(x: float, y: float) -> float:
    """
    Multiply 2 numbers.

    :param x: The first number to multiply.
    :param y: The second to multiple `x` by.
    :return: The product of `x` and `y`
    """
    result = x * y
    return result  # to find out what the function calculated
                   # and print it out later


def is_palindrome(string: str) -> bool:
    return string[::-1].casefold() == string.casefold()
    # returns True/False


def palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """
    return the `n` th Fibonacci number, for positive `n`.

    :param n: The amount of numbers in the sequence
    :return: The sum of the previous two numbers
    """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))




