"""
911 calls
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('911.csv')
print(df.info())
print()
print(df.head())
print()

# Get top five zip codes for 911 calls
print(df['zip'].value_counts().head(5))

print()

# Get top five townships for 911 calls
print(df['twp'].value_counts().head(5))

print()

# Look at title column. How many unique codes
print(df['title'].nunique())

print()

# Create a column 'Reason' containing EMS,Fire,Traffic
x = df['title'].iloc[0]
print(x)
print(x.split(':')[0])

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
print(df['Reason'].value_counts())

print()

sns.countplot(x='Reason',data=df)
plt.show()

df['timeStamp'] = pd.to_datetime(df['timeStamp'])

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
print(df['Hour'])

df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

print(df.head())

dmap = {0:'Mon',1:'Tue',3:'Wed',4:'Thu',5:'Fri',6:'Sat',7:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

print(df.head())

sns.countplot(x='Day of Week', data=df,hue='Reason')
plt.show()

byMonth = df.groupby('Month').count()
# print(byMonth['lat'].plot())
byMonth['lat'].plot()
plt.show()

sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())
plt.show()

t = df['timeStamp'].iloc[0]
df['Date'] = df['timeStamp'].apply(lambda t:t.date())
df.groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.show()







