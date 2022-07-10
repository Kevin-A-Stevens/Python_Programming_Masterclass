"""
tuples = an ordered set of data
immutable = cannot be changed
as below parentheses are optional but best to include them
As tuples are a sequence type, you can use indexing
reasons to use a tuple
Protect the integrity of your data
Can always unpack a tuple successfully
"""

t = "a", "b", "c"
print(t)  # ('a', 'b', 'c')

name = "Kevin"
age = 55

print(name, age, "Python", 2022)

# If you want a tuple, need parentheses in this case
print((name, age, "Python", 2022))

print()
# tuples are immutable
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[0] = "Master of Puppets" = gives an error (immutable)

# Create a list first, then make the change
metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)

