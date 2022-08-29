numbers = [1, 2, 3, 4, 5, 6]

squares = []
for number in numbers:
    squares.append(number ** 2)

print(squares)

# list comprehension

numbers = [1, 2, 3, 4, 5, 6]

squares = [number ** 2 for number in numbers]

print(squares)

# set comprehension

numbers = [1, 2, 3, 4, 5, 6]

squares = {number ** 2 for number in numbers}

print(squares)
