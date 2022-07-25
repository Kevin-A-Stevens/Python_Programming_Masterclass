"""
Zipping files

functions used
print()
zip()

methods used
.writerow()
.DictWriter()

"""
import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ['album', 'artist', 'year']

# first, find out what kind of data you are dealing with
for row in albums:
    print(row)

filename = 'albums.csv'
with open(filename, 'w',encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file,fieldnames=keys)
    writer.writeheader()
    # Create zip objects
    for row in albums:
        zip_object = zip(keys, row)
        # print(zip_object)
        # find out what things are in those objects
        # for thing in zip(keys, row):
        #     print("\t", thing)
        # Create dictionaries from the zip objects
        albums_dict = dict(zip_object)
        print(albums_dict)
        writer.writerow(albums_dict)

# albums.csv is created



