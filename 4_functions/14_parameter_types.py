"""
defining different parameter types

using **args and **kwargs

the keywords must come after the arguments
**kwargs uses a variable number of keywords

This is why the k is needed to pass its name
so Python will know when to stop with the arguments
passed to *args
"""


def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword:.................{}".format(k))
    print("var-keyword:.............{}".format(kwargs))


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)
