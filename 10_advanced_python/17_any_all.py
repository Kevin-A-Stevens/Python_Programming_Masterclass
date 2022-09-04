"""
any and all return True or False depending
on the values in the iterable

all = all values in the list are True values
any = at least one value is True
"""
entries = [1, 2, 3, 4, 5]
print("all: {}".format(all(entries)))  # True
print("any: {}".format(any(entries)))  # True

print("Iterable with a `False` value")
entries_with_zero = [1, 2, 0, 4, 5]
print("all: {}".format(all(entries_with_zero)))  # False
print("any: {}".format(any(entries_with_zero)))  # True
