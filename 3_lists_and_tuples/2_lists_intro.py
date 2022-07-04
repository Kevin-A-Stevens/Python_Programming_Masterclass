"""
introduction to lists
lists are a sequence type
lists are mutable (they can be changed)

"""
computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse pad"
                  ]

for part in computer_parts:
    print(part)

print()
print(computer_parts[2])
print(computer_parts[0:3])  # slicing a list produces another list
print(computer_parts[-1])
