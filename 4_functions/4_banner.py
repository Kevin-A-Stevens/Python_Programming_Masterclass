"""
not all functions return something useful

sometimes you want to write a function that
performs an action but does not return anything

handling invalid arguments with raise ValueError
(raise ExceptionType)

Setting default values
If not specified, the default value is used

functions used
print()
len()

methods used
.center()

"""


def banner_text(text, screen_width=80):
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*", 66)
banner_text("Always look on the bright side of life...", 66)
banner_text("If life seems jolly rotten,", 66)
banner_text("There's something you've forgotten!", 66)
banner_text("And that's to laugh and smile and dance and sing,", 66)
banner_text(" ", 66)
banner_text("When you're feeling in the dumps,", 66)
banner_text("Don't be silly chumps,", 66)
banner_text("Just purse your lips and whistle - that's the thing!", 66)
banner_text("And... always look on the bright side of life...", 66)
banner_text("*", 66)
