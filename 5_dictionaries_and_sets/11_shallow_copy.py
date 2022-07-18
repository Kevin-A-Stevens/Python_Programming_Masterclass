"""
mutable objects
shallow copy

functions used
print()

methods used
.copy() = creates a copy of the original dictionary

The difference between shallow and deep copy is when
we use lists instead of strings
"""
animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

# there is only one dictionary
# things = animals
# animals["teddy"] = "toy"
# print(things["teddy"])

# if we want another dictionary, we should use copy
things = animals.copy()
animals["teddy"] = "toy"
print(things["teddy"])
print(animals["teddy"])

print()

animals2 = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

things2 = animals2.copy()

print(things2["teddy"])
print(animals2["teddy"])

print()

things2["teddy"].append("toy")
print(things2["teddy"])
print(animals2["teddy"])
