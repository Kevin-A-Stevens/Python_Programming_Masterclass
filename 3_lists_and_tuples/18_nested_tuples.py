"""
nested tuples and lists
we have created tuples without using ()
it is recommended to use () and now
we will see why

functions used
print()
len()
"""
albums = ["Welcome to my Nightmare", "Alice Cooper", 1975,
          "Bad Company", "Bad Company", 1974,
          "Nightflight", "Budgie", 1981,
          "More Mayhem", "Emilda May", 2011,
          "Ride the Lightning", "Metallica", 1984,
          ]

print(len(albums))  # 15

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))  # 5

for album in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(album[0], album[1], album[2]))

print()
# more tidy is to unpack the tuples
# you will do it this way most of the time
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

print()
# another way
for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
