"""
buy computer

functions used
enumerate() = returns pairs of value (index and item)
print()
len()
str()

methods used
.append() = add items to a list
.remove() = remove items from a list

"""
available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse pad",
                   "hdmi cable",
                   "dvd drive",
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []

for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = "-"  # initialize current_choice
computer_parts = []  # create an empty list

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # if already in, remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from then list below: ")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)
