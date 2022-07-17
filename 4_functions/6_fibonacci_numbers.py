"""
fibonacci numbers
previous two numbers added together give
next number in the sequence
Ex: 0,1,1,2,3,5,8,13,21,34,55,89,144,...
"""


def fibonacci(n):
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
