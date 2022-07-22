"""
Deleting items from a set

functions used
print()

methods used
.clear() = removes all items from a set
.discard() = remove an item
.remove() = remove an item (errors if item does not exist)

Whether you use discard or remove depends on what you
want to achieve. If you just want an item gone, use
discard. If you want to know whether an item is removed
and let you know if the item exists or not, use remove
"""
small_ints = set(range(21))
print(small_ints)

print()

small_ints.clear()
print(small_ints)

print()
small_ints = set(range(21))
small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99)
print(small_ints)

