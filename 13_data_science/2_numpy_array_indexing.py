import numpy as np

arr = np.arange(0,11)
print(arr)

index_8 = arr[8]
print(index_8)

index_slice = arr[1:5]
print(index_slice)

index_slice2 = arr[0:5]
print(index_slice2)

up_to_six = arr[:6]
print(up_to_six)

five_to_end = arr[5:]
print(five_to_end)

# broadcast in an array (set first 5 values to 100)
arr[0:5] = 100
print(arr)

arr = np.arange(0,11)
print(arr)

slice_of_arr = arr[0:6]
print(slice_of_arr)

slice_of_arr[:] = 99
print(slice_of_arr)
print(arr) # The broadcast changed the original array also

# copying an array
arr_copy = arr.copy()
print(arr)
print(arr_copy)
arr_copy[:] = 100
print(arr_copy)
print(arr)

# Create a 2d array or 2d matrix
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)

first_index = arr_2d[0][0]  # double bracket method
print(first_index)
second_index = arr_2d[2][1]
print(second_index)

# Use the single bracket method as it's less prone to error
third_index = arr_2d[1,2]  # single bracket method
print(third_index)

# get parts of an array using slicing
array_part = arr_2d[:2,1:]
print(array_part)

# conditional selection
arr = np.arange(1,11)
print(arr)
bool_array = arr > 5
print(bool_array)
print(arr[bool_array])  # returns where instances were True

less_than_three = arr[arr<3]
print(less_than_three)




