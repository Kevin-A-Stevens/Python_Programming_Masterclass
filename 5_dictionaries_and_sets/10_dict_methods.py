"""
dictionary methods

functions used
print()

methods used
.fromkeys() = creates a dictionary from a sequence like a list
.keys() = returns a list of keys in a tuple
when you see .keys, you know you are dealing with a dict
.update() = updates one dictionary with values from another
.values() = returns a list of values in a tuple

"""
d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

d2 = {
    7: "luck seven",
    10: "ten",
    3: "this is the new three",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

new_dict = dict.fromkeys(pantry_items, 0)
print(new_dict)

keys = d.keys()
print(keys)

for item in d.keys():
    print(item)

# does the same as above but using .keys() above is more clear
for item in d:
    print(item)

d.update(d2)
for key, value in d.items():
    print(key, value)

print()

# can also use enumerate with .update()
d.update(enumerate(pantry_items))
for key, value in d.items():
    print(key, value)

v = d.values()
print(v)


