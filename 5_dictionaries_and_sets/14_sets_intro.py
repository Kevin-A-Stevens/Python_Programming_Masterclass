"""
sets

an unordered collection with no duplicate entries

A set uses {}
A list uses []
A tuple uses ()
A dictionary uses {} but contains key-value pairs

sets use hashes so anything you want to put in a set
must be hashable. Dictionary keys also have this
requirement

This is the reason you cannot put a list in a set
and will get an 'unhashable type' error

cannot index or slice a set
"""

# note the order changes every time the program is run
farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print()

print("Indexing a sequence")
animals_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animals_list[3]
print(goat)

# print("Indexing a set is not possible")
# goat = farm_animals[3]

# sets are equal if they contain the same items
# regardless of order
more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
if more_animals == farm_animals:
    print('The sets are equal')
else:
    print("The sets are different")
