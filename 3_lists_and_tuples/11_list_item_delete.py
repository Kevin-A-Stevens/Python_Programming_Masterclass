"""
deleting an item from a list
"""
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# delete items manually with del
# del data[0:2]
# print(data)
#
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
        if value >= min_valid:
                stop = index
                break

print(stop)
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
        if data[index] <= max_valid:
                # we have the index the last item to keep
                # set 'start' to the position of the first
                # item to delete, which is 1 after the index
                start = index + 1
                break

print(start)
del data[start:]
print(data)
print()

# as the index numbers change when iterating over a list
# forwards, removing items starting at the end may be
# a better option

data = [104, 101, 4, 105, 308, 103, 5,
           107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

for index in range(len(data) -1, -1, -1):
        if data[index] < min_valid or data[index] > max_valid:
                print(index, data)
                del data[index]

print(data)





