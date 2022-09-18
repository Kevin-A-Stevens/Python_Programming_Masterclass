"""
Linear Regression project
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

customers = pd.read_csv('Ecommerce Customers')
print(customers.head())

sns.jointplot(data=customers,x='Time on Website',y='Yearly Amount Spent')
plt.show()

sns.jointplot(data=customers,x='Time on App',y='Yearly Amount Spent')
plt.show()

sns.jointplot(data=customers,x='Time on App',y='Length of Membership',kind='hex')
plt.show()

sns.pairplot(customers)
plt.show()

sns.lmplot(data=customers,x='Length of Membership',y='Yearly Amount Spent')
plt.show()

print(customers.columns)

y = customers['Yearly Amount Spent']
X = customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
lm = LinearRegression()
lm.fit(X_train,y_train)

print(lm.coef_)
predictions = lm.predict(X_test)

plt.scatter(y_test,predictions)
plt.xlabel('Y test (True Values)')
plt.ylabel('Predicted Values')
plt.show()

print()
print('MAE ',metrics.mean_absolute_error(y_test,predictions))
print('MSE ',metrics.mean_squared_error(y_test,predictions))
print('RMSE ',np.sqrt(metrics.mean_squared_error(y_test,predictions)))

sns.distplot((y_test-predictions),bins=50)
plt.show()

cdf = pd.DataFrame(lm.coef_,X.columns,columns=['Coeff'])
print(cdf)


