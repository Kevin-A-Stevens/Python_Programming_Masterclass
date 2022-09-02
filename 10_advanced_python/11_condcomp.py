"""
Conditional Comprehensions
"""
menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meals)

# conditional comprehension
# meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)

fussy_meals = [meal for meal in menu if "spam" or "eggs" in meal if not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

x = 12
expression = "Twelve" if x == 12 else "unknown"
print(expression)

meals1 = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
print(meals1)

for meal in menu:
    print(meal, "contains sausage" if "sausage" in meal else "contains bacon" if "bacon" in meal else "contains egg")

print()

items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)

print()

for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal, item))
            break

for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)

fizzbuzz = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
            for x in range(1, 31)]
print(fizzbuzz)

