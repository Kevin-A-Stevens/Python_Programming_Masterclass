"""
using break
break exits the loop completely

We'll be using a list
a list is an ordered sequence of values enclosed in []

functions used
len() = gives how many items are in a sequence
print()
"""

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

# for index in range(6):
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))


