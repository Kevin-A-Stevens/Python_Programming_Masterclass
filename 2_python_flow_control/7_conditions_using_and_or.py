"""
Conditions using and/or
and = either expression evaluates to True
or = both or all expressions evaluate to True
"""

age =int(input("How old are you? "))

if age >= 16 and age <= 65:
    print("Have a good day at work")

# Simplify chained comparisons
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")
    