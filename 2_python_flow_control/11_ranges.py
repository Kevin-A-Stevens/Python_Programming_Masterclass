"""
using the range function

functions used
range() = (start, end, step) not including the end number
start value defaults to 0 if not included
print()

"""

for i in range(21):
    print("i is now {}".format(i))

print("*" * 80)

for i in range(0, 21, 2):
    print("i is now {}".format(i))

print("*" * 80)

# count backwards
for i in range(21, 0, -2):
    print("i is now {}".format(i))

# can use 'in' in range also
age = 55
if age in range(16, 66):
    print("Have a good day")
