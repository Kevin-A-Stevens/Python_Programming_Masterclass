"""
using continue
continue interrupts the normal flow of the loop and
either jumps out of it or stops current iteration and moves
on to the next one

We'll be using a list
a list is an ordered sequence of values enclosed in []
"""

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)
