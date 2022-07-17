"""
dictionaries

dictionaries and sets are not sequences
we cannot access them using index positions

instead, we use a key to get individual values
from that dictionary

dictionaries store key-value pairs
also referred to as mapping

A set is an unordered collection of items
We'll see sets later

functions used
print()

methods used
.get()

One reason to use .get is if the key does not exist,
.get() returns None. with indexing, your program
will crash if the ['key'] does not exist

One reason to use indexing is it is faster. Use
indexing if you are sure the key exists
use .get() if you are not sure the key is present

Sometimes you want to get an error. Use indexing
in this case. Sometimes, it is better for the program
to crash than to process invalid data
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

# use the key instead of the index to get the value
my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

# dictionaries also have a get method
learner = vehicles.get("er5")
print(learner)

