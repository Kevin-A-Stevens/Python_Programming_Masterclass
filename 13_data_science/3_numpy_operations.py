import numpy as np

arr = np.arange(0,11)
print(arr)

add_two_arrays = arr + arr
print(add_two_arrays)

subtract_two_arrays = arr - arr
print(subtract_two_arrays)

multiply_two_arrays = arr * arr
print(multiply_two_arrays)

# scalar operations
add_100 = arr + 100
print(add_100)

multiply_array = arr * 100
print(multiply_array)

exponent_array = arr ** 3
print(exponent_array)

square_root = np.sqrt(arr)
print(square_root)

exponential_array = np.exp(arr)
print(exponential_array)

print(np.max(arr))

array_sin = np.sin(arr)
print(array_sin)
