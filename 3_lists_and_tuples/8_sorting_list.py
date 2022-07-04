"""
sorting a list = two ways to sort

functions used
print()
sorted() = sort any iterable object. returns a different list

methods used
.extend() = adds a list to a list
.sort() = sorts a list in place and returns None
"""
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)
another_even = even
print(another_even)

even.sort()
print(even)

even.sort(reverse=True)
print(even)
print(another_even)

pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()  # in place sort
print(numbers)

another_sorted_numbers = numbers.sort()
print(numbers)
print(another_sorted_numbers)

# case insensitive sorting
missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham",
        "John",
        "terry",
        "eric",
        "Terry",
        "michael",
        ]
names.sort(key=str.casefold)
print(names)
