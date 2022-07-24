"""
read, readline, and readlines

functions used
open()
reversed()

methods used
.readlines() = outputs a list of strings
.read() = outputs a string
.readline() = read file line by line and perform
            an action when you find what you
            are looking for

"""
with open('jabberwocky.txt', 'r') as jabber:
    lines = jabber.readlines()

print(lines)
print(lines[-1:])

# process lines in reverse order
for line in reversed(lines):
    print(line, end='')

with open('jabberwocky.txt', 'r') as jabber:
    text = jabber.read()

print(text)

# reverse entire contents of a file
for character in reversed(text):
    print(character, end='')

with open('jabberwocky.txt', 'r') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break  # break if jubjub is found

print("*" * 80)

with open('jabberwocky.txt', 'r') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break

