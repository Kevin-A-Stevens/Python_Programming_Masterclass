"""
generator example

A generator works like an iterator
"""
import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


# big_range = range(1000)
# big_range = my_range(1000)
big_range = my_range(5)

# We can use next in a generator
print(next(big_range))
# print size before it has any values in it (memory use)
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []
for val in big_range:
    big_list.append(val)

# print size of big_list with values in it (memory use)
print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

print("looping again ... or not")
for i in big_range:
    print("i is {}".format(i))


