## Import the required libraries
import pandas as pd
import numpy as np

## Read the data
data=pd.read_csv('stock.csv')

## Creating a variable for daily returns
data['daily_return']=data['Close']-data['Open']

Avg_daily_return=data['daily_return'].mean()

print(f"Average Daily Return: {Avg_daily_return}")
print('***'*20)
print()

print(f"Maximum Daily Return: {data['daily_return'].max()}")
print('***'*20)
print()

print(f"Minimum Daily Return: {data['daily_return'].min()}")
print('***'*20)
print()

data['diff']=data['daily_return'].apply(lambda x:x-Avg_daily_return)

deviation=np.sqrt((data['diff'].sum())**2/len(data))

print(f"Standard Deviation of Daily Return: {deviation}")

