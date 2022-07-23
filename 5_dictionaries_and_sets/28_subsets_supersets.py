"""
Subsets and supersets

Can also use <= and < as operators for subsets
Use >= and > for supersets

Just as before, these operators can only be used with sets

Functions used
print()

Methdos used
.issubset()  < and <=
.issuperset()  > and >=

"""
animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat',
           }

birds = {'Robin', 'Swallow', 'Wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f'animals is a superset of birds: {animals.issuperset(birds)}')

print(birds <= animals)
print(birds < animals)

print("*" * 80)

garden_birds = {'Swallow', 'Wren', 'Robin'}
print(garden_birds == birds)  # True - both sets are equal
print(garden_birds <= birds)  # True - is a subset of birds
print(garden_birds < birds)  # False - not a proper subset

print("*" * 80)

more_birds = {'Wren', 'Budgie', 'Swallow'}
print(garden_birds >= more_birds)  # False




