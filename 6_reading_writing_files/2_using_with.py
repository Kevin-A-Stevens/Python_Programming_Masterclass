"""
Using with in Python

Opening a file this way is preferred because the file
will automatically be closed when the with block
terminates

functions used
open()
print()

methods used
.rstrip()

"""
with open('jabberwocky.txt', 'r') as jabber:
    for line in jabber:
        print(line.rstrip())


