"""
Machine Learning with Python
We will be using scikit Learn

pip3 install scikit-learn

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('USA_Housing.csv')

# Get info about your data
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()
print(df.columns)

sns.pairplot(df)
plt.show()

sns.distplot(df['Price'])
plt.show()

sns.heatmap(df.corr(),annot=True)
plt.show()
