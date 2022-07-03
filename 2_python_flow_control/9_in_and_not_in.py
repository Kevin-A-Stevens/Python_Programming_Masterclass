"""
Using 'in' and 'not in'

functions used
print()
input()
casefold() = ignore case
int()

"""
parrot = "Norwegian Blue"

letter = input("enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")

print("*" * 80)

activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")

#  If challenge
name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome club 18-30 holidays, {0}".format(name))
else:
    print("I'm sorry, our holidays are not available for your age group")
