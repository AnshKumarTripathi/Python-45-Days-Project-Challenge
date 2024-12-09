import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("D:/45-Days-Challege-JS-Python/all_billionaires_1997_2024.csv")

df['net_worth'] = df['net_worth'].replace({' B': ''}, regex=True).astype(float) * 1e9

df = df[['year', 'net_worth']].dropna()

X = df[['year']]  
Y = df['net_worth']  

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

plt.scatter(X, Y, color='blue', alpha=0.5, label='Data Points')
plt.plot(X_test, Y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Net Worth')
plt.title('Year vs Net Worth Linear Regression')
plt.legend()
plt.show()
