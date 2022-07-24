"""
reading text files

functions used
open()
print()

methods used
.close()
.strip()

"""
# open the file
jabber = open('jabberwocky.txt', 'r')

# read the file
for line in jabber:
    # print(line)
    # print(line, end='')  # Get rid of extra new line
    print(line.strip())  # remove newline from end of string

# close the file
jabber.close()

# Our output is double-spaced because there is
# a new line character at the end of each line
# The print functions defaults to printing \n
# Therefore, we get two new lines printed
# Two ways to deal with this as shown above
