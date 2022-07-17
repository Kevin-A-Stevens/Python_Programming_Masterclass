"""
Adding items to a dictionary

dictionaries to not have an append method
we assign values to a dictionary using a key
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

# add new entry to dictionary
vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# more efficient to use the .items() method
for key, value in vehicles.items():
    print(key, value, sep=", ")
