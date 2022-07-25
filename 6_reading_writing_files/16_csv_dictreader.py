"""
The CSV module provides other classes useful
when parsing or writing csv files

The DictReader works like the reader we've
seen already but produces rows of dictionaries

functions used
print()

methods used
.DictReader()

"""
import csv

cereals_filename = 'cereal_grains.csv'

with open(cereals_filename, encoding='utf-8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)

