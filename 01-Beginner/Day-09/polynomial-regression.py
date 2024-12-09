import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("D:/45-Days-Challege-JS-Python/all_billionaires_1997_2024.csv")

df['net_worth'] = df['net_worth'].replace({' B': ''}, regex=True).astype(float) * 1e9

df = df[['year', 'net_worth']].dropna()

df['log_net_worth'] = np.log(df['net_worth'])

X = df[['year']]
Y = df['log_net_worth']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)
Y_pred_exp = np.exp(Y_pred)  
mse = mean_squared_error(np.exp(Y_test), Y_pred_exp)
r2 = r2_score(np.exp(Y_test), Y_pred_exp)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

plt.scatter(X, np.exp(Y), color='blue', alpha=0.5, label='Data Points')
X_plot = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
Y_plot = model.predict(X_plot)
Y_plot_exp = np.exp(Y_plot)  
plt.plot(X_plot, Y_plot_exp, color='red', linewidth=2, label='Exponential Regression Line')
plt.xlabel('Year')
plt.ylabel('Net Worth')
plt.title('Year vs Net Worth Exponential Regression')
plt.legend()
plt.show()
