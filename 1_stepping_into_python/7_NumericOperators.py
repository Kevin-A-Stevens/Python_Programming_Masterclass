"""
Numeric Operators

Functions used"
print()
range() - must use integers
"""
a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0  division gives a float
print(a // b)  # 4 integer division rounds down
print(a % b)  # 0 modulo: remainder

print()

for i in range(1, 4):
    print(i)

for i in range(1, a // b):
    print(i)
