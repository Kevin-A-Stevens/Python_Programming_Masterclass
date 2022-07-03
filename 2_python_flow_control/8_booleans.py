"""
Booleans are either True or False
0 = False
Empty sequences = False
"""
day = "Monday"
temperature = 30
raining = True

if day == "Saturday" and temperature > 27 and not raining:
    print("Go swimming")
else:
    print("Learn Python")

name = input("Please enter your name: ")
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")


