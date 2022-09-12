import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
titanic.head()

sns.jointplot(x='fair',y='age',data=titanic)
plt.show()

sns.distplot(titanic['fair'])
plt.show()

sns.boxplot(x='class',y='age',data=titanic)
plt.show()
