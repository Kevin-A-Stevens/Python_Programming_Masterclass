import numpy as np

my_list = [1, 2, 3]
arr = np.array(my_list)
print(arr)

print()

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
multi_arr = np.array(my_mat)
print(multi_arr)

print()
# creating am array range
my_range = np.arange(0,11)
print(my_range)
my_range_step = np.arange(0,11,2)
print(my_range_step)

# create zeros
my_zeros = np.zeros(3)
print(my_zeros)
my_zeros_multi = np.zeros((2,3))
print(my_zeros_multi)

# create ones
my_ones = np.ones((2,3))
print(my_ones)

# linspace
my_linespace = np.linspace(0,5,10)
print(my_linespace)

print()
# creating an identity matrix
id_matrix = np.eye(4)
print(id_matrix)

# craeting an array of random numbers 0 to 1
rand_num = np.random.rand(5)
print(rand_num)

rand_num2 = np.random.rand(5,5)
print(rand_num2)

randn_num = np.random.randn(2)
print(randn_num)

randn_num2 = np.random.randn(2,2)
print(randn_num2)

print()
# get random int
rand_int = np.random.randint(1,100)
print(rand_int)

# 10 random ints
ten_rand_ints = np.random.randint(1,100,10)
print(ten_rand_ints)

print()
arr = np.arange(25)
print(arr)
ranarr = np.random.randint(0, 50, 10)
print(ranarr)

# reshaping an array
new_shape = arr.reshape(5,5)
print(new_shape)

# get max
max_num = ranarr.max()
# get min
min_num = ranarr.min()
print(max_num)
print(min_num)

# get index location of max num
index_loc = ranarr.argmax()
print(index_loc)
# get index location of min num
index_loc2 = ranarr.argmin()
print(index_loc2)

# get shape of array
arr_shape = arr.shape
print(arr_shape)

# get data type
arr_data_type = arr.dtype
print(arr_data_type)
