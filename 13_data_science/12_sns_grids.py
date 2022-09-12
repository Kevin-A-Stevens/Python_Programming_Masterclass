import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = sns.load_dataset('iris')
iris.head()

sns.PairGrid(iris)
plt.show()
