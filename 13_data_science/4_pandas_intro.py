"""
Pandas was built on top of numpy
Excels in performance and productivity
Can work with a wide variety of data
need to pip3 install pandas
"""
import numpy as np
import pandas as pd

# A series can have access labels
labels = ["a", "b", "c"]
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

# We have four python objects
# create a series
my_series = pd.Series(data=my_data)
print(my_series)

my_labels = pd.Series(data=my_data, index=labels)
print(my_labels)

# This does the same
my_labels2 = (pd.Series(my_data,labels))
print(my_labels2)

np_array = pd.Series(arr, labels)
print(np_array)

dict_series = pd.Series(d)
print(dict_series)

ser1 = pd.Series([1, 2, 3, 4], ['USA', "Germany", 'Japan', 'Ireland'])
print(ser1)

ser2 = pd.Series([1, 2, 5, 4], ['USA', "Germany", 'Italy', 'Japan'])
print(ser2)

print(ser1['USA'])

ser3 = pd.Series(data=labels)
print(ser3)

# Can add two or more series together
print(ser1 + ser2)

