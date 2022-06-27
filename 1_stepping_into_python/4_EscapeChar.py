"""
Escape characters

Functions used:
print()
"""

# new line
splitString = "This strings has been\nsplit over\nseveral\nlines"
print(splitString)

# tab
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# escape character
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

# Using """
print("""The pet shop owner said "No, no, 'e's uh,...he's resting". """)

anotherSplitString = """This string has been
split over
several
lines"""
print(anotherSplitString)

# The \ cna escape an end of the line
anotherWaySplitString = """This string has been \
split over \
several \
lines"""
print(anotherWaySplitString)

# including the \ character in strings
print("C:\\Users\\tim\\notes.txt")
print(r"C:\Users\tim\notes.txt")

