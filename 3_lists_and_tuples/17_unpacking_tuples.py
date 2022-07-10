"""
unpacking tuples
"""
a = b = c = d = e = f = 12
print(c)

# unpacking
x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")
data = 1, 2, 76  # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

# You can unpack any sequence type
print("Unpacking a list")
data_list = [12, 13, 14]
p, q, r = data_list
print(p)
print(q)
print(r)

# Practical uses for unpacking a tuple
for t in enumerate("abcdefgh"):
    print(t)

print()
for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

# More unpacking
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# unpack the tuple
title, artist, year = metallica
print(title)
print(artist)
print(year)

print()
table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

# give  variable names to make it obvious
# what you are printing when you unpack
name, length, width, height, price = table
print(length * width)

