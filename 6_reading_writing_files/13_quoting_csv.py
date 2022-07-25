"""
Properly quoted csv files are easy for the
csv module to read

Notice that all numerical values are read as strings

We can use the quoting argument to tell Python how
the data has been quoted
"""
import csv

csv_filename = 'cereal_grains.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)

