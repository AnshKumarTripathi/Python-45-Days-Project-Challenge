import pandas as pd

df = pd.read_csv('D:/45-Days-Challege-JS-Python/traffic.csv')

print(df.head())

print(df.describe())

print(df.isnull().sum())



df.fillna(df.mean(), inplace=True)
df.dropna(inplace=True)


# Filter data based on a condition
filtered_df = df[df['Junction'] == 'Junction 1']

# Calculate the average traffic count per hour
avg_traffic_per_hour = filtered_df.groupby('Hour')['Traffic_Count'].mean()
print(avg_traffic_per_hour)

# Plot traffic trends over time
import matplotlib.pyplot as plt

filtered_df.groupby('Date')['Traffic_Count'].sum().plot()
plt.title('Daily Traffic Count at Junction 1')
plt.xlabel('Date')
plt.ylabel('Total Traffic Count')
plt.show()
