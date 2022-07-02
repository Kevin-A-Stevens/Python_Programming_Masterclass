"""
Slicing in Python
[start:end but not including:step]
"""
parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian
print(parrot[:9])  # Norwegian
print(parrot[10:14])  # Blue
print(parrot[10:])  # Blue

print(parrot[:6])  # Norweg
print(parrot[6:])  # ian Blue

print(parrot[:6] + parrot[6:])  # Norwegian Blue
print(parrot[:])  # Norwegian Blue

# Using negative numbers
print(parrot[-4:-2])  # Bl
print(parrot[-4:12])  # Bl

# Using a step in a slice
print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)  # ,;: ,;

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

# Slicing backwards
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]  # Python Idiom reversing a sequence
print(backwards)

print(letters[16:13:-1])  # qpo
print(letters[4::-1])  # edcba
print(letters[:-9:-1])  # zyxwvuts = last 8 characters


# Common Idioms
print(letters[-4:])  # wxyz = last 4 letters
print(letters[-1:])  # z = last item
print(letters[:1])  # a = first character
print(letters[0])  # a = first character (errors if string is empty)















