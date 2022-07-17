"""
removing items from a dictionary

can use del to remove items but the program
will crash if the key does not exist

methods used
.pop() = can use a default value
the default value of None will return None
if the key does not exist instead of crashing

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

# changing a value in a dictionary
vehicles["virago"] = "Yamaha XV535"

# removing a value from a dictionary
del vehicles["starfighter"]
result = vehicles.pop("f1", "Does not exist")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not found")
print(bike)


print()

# more efficient to use the .items() method
for key, value in vehicles.items():
    print(key, value, sep=", ")
