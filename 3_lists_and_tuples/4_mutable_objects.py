"""
a mutable object can be changed

mutable objects are
list, dict, set, Bytearray
"""
shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice",
                 ]

another_list = shopping_list
print(id(shopping_list))  # same id
print(id(another_list))  # same id

shopping_list += ["cookies"]
print(shopping_list)

print(id(shopping_list))  # id is the same as above
print(another_list)  # same as shopping_list (object)

a = b = c = d = e = f = another_list
print(a)
print("Adding cream")
b.append("cream")
print(c)
print(d)

# There is still only one object; the object is known by
# different names




