"""
mutable objects
shallow copy

functions used
print()

methods used
.copy() = creates a copy of the original dictionary

The difference between shallow and deep copy is when
we use lists instead of strings

a shallow copy copies references. It doesn't make a copy
of the things being referred to. Below the key references
are copied to a new dictionary but there is still only
one list and both dictionaries are referring to it
"""
lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]
animals2 = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

# things2 = animals2.copy()
things2 = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

print(things2["teddy"])
print(animals2["teddy"])

print()

# things2["teddy"].append("toy")
teddy_list.append("toy")
animals2["teddy"].append("added via `animals`")
things2["teddy"].append("added via `things`")
print(things2["teddy"])
print(animals2["teddy"])
print(teddy_list)

