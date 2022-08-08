"""
Defining our own functions continued

The *args argument means any amount of arguments
It does not have to be named *args but is usually
seen this way and is recommended

"""
# Define the function


def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


# Call the function
python_food()

center_text("My spam and eggs")
center_text("Spam, spam, and eggs")
center_text(12)
center_text("Spam, spam, spam, and eggs")

center_text("first", "second", 3, 4, "spam", sep=":")

