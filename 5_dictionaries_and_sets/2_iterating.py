"""
iterating over a dictionary

functions used
print()

methods used
.items()

use enumerate when iterating over sequences
use .items() when iterating over dictionaries

"""
vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

# when iterating over a dictionary, you are iterating over the keys
for key in vehicles:
    print(key)

print()

# to get both keys and values, use indexing
for key in vehicles:
    print(key, vehicles[key], sep=", ")

print()

# more efficient to use the .items() method
for key, value in vehicles.items():
    print(key, value, sep=", ")

