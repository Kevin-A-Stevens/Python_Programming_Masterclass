"""
the setdefault method

returns the value of a key of the key exists
if the key does not exist returns the default
value we specify and adds it to the dictionary

This is different from the .get() method which
returns the value but does not add item to the
dictionary

The default value does not have to be a number

functions used
print()

methods used
.setdefault()

"""
from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

print()
print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)
