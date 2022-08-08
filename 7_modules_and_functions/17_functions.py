"""
Writing output to a file

Now that we are using return, we can use print
"""
# Define the function


def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


with open("menu", mode='w') as menu:
    # Call the function
    print(center_text("My spam and eggs"), file=menu)
    print(center_text("Spam, spam, and eggs"), file=menu)
    print(center_text(12), file=menu)
    print(center_text("Spam, spam, spam, and eggs"), file=menu)
    print(center_text("first", "second", 3, 4, "spam", sep=":"), file=menu)
