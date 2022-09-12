"""
Seaborn Matrix Plots
"""
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()
flights.head()
tc = tips.corr()

# sns.heatmap(tc,annot=True,cmap='coolwarm')
# plt.show()

print(flights)
print(tips)

fp = flights.pivot_table(index='month',columns='year',value='passengers')
sns.heatmap(fp,annot=True,cmap='coolwarm')
plt.show()
