"""
Data visualization example with Pandas
"""

import pandas as pd

# READ

df = pd.read_csv('ArgentinaCPI.csv')
print(df['time'])
print(df['value'])

# WRITE

names = ['Wade', 'James', 'Kobe', 'Curry']
total = [55, 50, 44, 36]
data_set = list(zip(names, total))
data_frame = pd.DataFrame(data=data_set, columns=['Names', 'Total'])
data_frame.to_csv('points.csv', index=True, header=True)
