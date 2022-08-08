"""
Defining our own functions

No return statement in the function means the function returns None
"""
# Define the function


def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(text):
    text = str(text)  # confirm text will convert to a string
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# Call the function
python_food()
print(python_food())

center_text("My spam and eggs")
center_text("Spam, spam, and eggs")
center_text(12)
center_text("Spam, spam, spam, and eggs")



