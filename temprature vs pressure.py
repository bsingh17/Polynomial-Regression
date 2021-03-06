import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('e1.csv')
x=dataset.iloc[:,0:1].values
y=dataset.iloc[:,1].values

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(x,y)

from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=4)
x_poly=poly.fit_transform(x)
poly.fit(x_poly,y)
reg2=LinearRegression()
reg2.fit(x_poly,y)

plt.scatter(x,y,color='blue')
plt.plot(x,reg.predict(x),color='red')
plt.title('Linear Regression')
plt.xlabel('Temprature')
plt.ylabel('Pressure')

plt.scatter(x,y,color='blue')
plt.plot(x,reg2.predict(x_poly),color='red')
plt.title('Polynomial Regression')
plt.xlabel('Temprature')
plt.ylabel('Pressure')

