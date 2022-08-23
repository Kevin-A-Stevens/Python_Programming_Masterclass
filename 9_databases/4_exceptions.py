"""
two types pf errors
Syntax errors = mistakes in the code
Exceptions = program logic

try: except: except: else: finally in that order
things you may want in your finally clause are close the db,
close open files, etc
"""


def factorial(n):
    # n! can also be defined as n * (n -1)
    """ Calculate ne recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    print(factorial(900))
except (RecursionError, OverflowError):
    print("This program cannot calculate factorials this large")
else:
    print("factorial was successful")
finally:
    print("The finally clause always executes")

print("Program terminating")




