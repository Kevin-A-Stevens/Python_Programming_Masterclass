"""
Writing data to a text file

methods used
.write()

Note the print function calls a special method, that all
objects have, before printing the object.

The method is called __str__
This method returns a string representation of the object

text files can only hold text
If you try and put numbers in a text file, it will not work

file modes
r, w, x, a, b, t, +

"""
data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

plants_filename = "flower_write.txt"

with open(plants_filename, "w") as plants:
    for plant in data:
        plants.write(plant)

print(data)
string_representation = data.__str__()
print(type(string_representation))

filename = "test_numbers.txt"

# works
with open(filename, "w") as test:
    for i in range(10):
        print(i, file=test)

# will not work
# with open(filename, "w") as test:
#     for i in range(10):
#         test.write(i)

# need to convert i to a string
with open(filename, "w") as test:
    for i in range(10):
        test.write(str(i) + "\n")
