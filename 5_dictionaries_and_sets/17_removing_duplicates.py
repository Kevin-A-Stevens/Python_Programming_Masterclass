"""
Removing duplicate values using sets
"""
data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from the list, to remove duplicates
unique_set = set(data)
print(unique_set)

# If you need sorted data
unique_sorted_data = sorted(set(data))
print(unique_sorted_data)

# Create a list of unique colors, keeping the order they appeared
unique_data_order = list(dict.fromkeys(data))
print(unique_data_order)

print()
print(dict.fromkeys(data))


