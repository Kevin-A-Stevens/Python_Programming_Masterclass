"""
set membership

use 'in' to test membership in a set

sets are faster when testing membership

a list for example, Python tests each member until
it finds what it is looking for called a linear search

a set, Python uses the hash code to find out where the item
should be. Hash codes are used in the same way as
dictionary keys

You can check set membership in 1 billion items
just a fast as a set with 5 items

"""
choice = "-"  # initialise choice to something invalid
while choice != "0":
    if choice in set("12345"):
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()
