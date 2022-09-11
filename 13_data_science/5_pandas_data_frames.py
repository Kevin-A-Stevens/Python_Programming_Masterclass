"""
Pandas Data Frames
"""
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

# build a dataframe
df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

w_col = df['W']
print(w_col)

print(type(df['W']))

my_col = df[['W','Z']]
print(my_col)

# Create a new column
df['new'] = df['W'] + df['Y']
print(df)

# Remove a column
df.drop('new', axis=1)  # drops the new column
print(df)

df.drop('E', axis=0)
print(df)

# ROWS
print(df)

my_rows = df.loc['A']
print(my_rows)

my_rows2 = df.iloc[0]
print(my_rows2)

my_b_y_loc = df.loc['B','Y']
print(my_b_y_loc)

my_subset = df.loc[['A', 'B'],['W', 'Y']]
print(my_subset)

# Check conditionals
print(df > 0)

print(df['W']>0)

print(df['Z']<0)
print(df[df['Z']<0])

results_df = df[df['W']>0]
print(results_df)
print(results_df['X'])

# Nice quick way to create a list
newindx = 'CA NY WY OR CO'.split()
print(newindx)

# Add new column
df['States'] = newindx
print(df)

