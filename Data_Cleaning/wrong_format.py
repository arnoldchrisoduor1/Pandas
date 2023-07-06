import pandas as pd

#Converting columns of date value to date format in a Dates column
df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'])
#Values that are not in the date time format will return
#Nat - not a time which can be removed by dropna.

df.dropna(subset=['Date'], inplace=True)