"""
Seaborn is a stat plotting library
It is built on top of matplotlib
install with pip3 install seaborn
"""
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# print(tips.head())

# sns.distplot(tips['total_bill'],kde=False,bins=30)
# plt.show()
#
# sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')
# plt.show()

# sns.pairplot(tips,hue='sex')
# plt.show()

sns.rugplot(tips['total_bill'])
plt.show()
