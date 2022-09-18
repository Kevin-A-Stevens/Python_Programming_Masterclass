"""
Logistic Regression
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Create data frame
train = pd.read_csv('titanic_train.csv')

print(train.head())

# Find missing data - note Age, Cabin, and Established columns
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

# Set stype of the grid you like
sns.set_style('whitegrid')

# Create count plot between survivors and non survivors
sns.countplot(x='Survived',data=train)
plt.show()

# Create a count plot separate by male/female
sns.countplot(x='Survived',hue='Sex',data=train, palette='RdBu_r')
plt.show()

# Create a count plot separate by passenger class
sns.countplot(x='Survived',hue='Pclass',data=train)
plt.show()

# Create a distribution chart based on age on board
sns.distplot(train['Age'].dropna(),kde=False,bins=30)
plt.show()

# Get list of columns
print(train.info())

# Look at the SibSp = how many siblings/spouse
sns.countplot(x='SibSp',data=train)
plt.show()

# get fare people spent
train['Fare'].hist(bins=40,figsize=(10,4))
plt.show()

# Deal with missing data

plt.figure(figsize=(10,7))
sns.boxplot(x="Pclass",y='Age',data=train)
plt.show()


def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):

        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age


train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

# Drop Cabin column. Too much missing information
train.drop('Cabin',axis=1,inplace=True)

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

# Drop the remaining missing value in Embarked as there is only one
train.dropna(inplace=True)

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

# We need to transform the Male/Femail to 0 and 1
# This is done so the ML algorythm can understand it

sex = pd.get_dummies(train['Sex'],drop_first=True)
embark = pd.get_dummies(train['Embarked'],drop_first=True)

train = pd.concat([train,sex,embark],axis=1)
print(train)

# drop columns you are not going to use
train.drop(['Sex','Embarked','Name','Ticket','PassengerId'],axis=1,inplace=True)

train = pd.concat([train,sex,embark],axis=1)
print(train)

# Build a training model
X = train.drop('Survived',axis=1)
y = train['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Create a model
logmodel = LogisticRegression()

# Train the model
logmodel.fit(X_train,y_train)

# Make predictions off the training model using test set
predictions = logmodel.predict(X_test)

print(classification_report(y_test,predictions))








