"""
Sniffer and Dialect

Sniffer can determine how the data is separated
and correctly process that data

functions used
print()
repr() = in the case of strings, includes \n
    often useful for diagnosing bugs

methods used
.readline()
.Sniffer()
.sniff()
.reader()
"""
import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3):  # get a sample for the first 3 lines
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    # country_dialect.skipinitialspace = True
    countries_data.seek(0)  # position file pointer at start of file
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print('*' * 80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    print(f'{attribute}: {repr(getattr(country_dialect, attribute))}')

