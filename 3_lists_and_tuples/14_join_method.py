"""
The join method

functions used
print()
len()
range()

methods used
.join() = string method. Iterates over a list for us
note - all items must be strings if you want to use join

"""
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))

print("*" * 80)

flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

for flower in flowers:
    print(flower)

print("*" * 80)

separator = ", "
output = separator.join(flowers)
print(output)

print(", ".join(flowers))
