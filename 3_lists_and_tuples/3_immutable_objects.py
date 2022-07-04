"""
immutable objects are
int, float, bool, str, tuple, frozen set, bytes

functions used
print()
id() = returns the identity of an object
"""
result = True
another_result = result
print(id(result))  # 9476448
print(id(another_result))  # 9476448

result = False
print(id(result))  # 9474016

# because a bool is immutable, we can not assign a new value
# to result. Instead the name result was attached a new value

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))  # different ID





