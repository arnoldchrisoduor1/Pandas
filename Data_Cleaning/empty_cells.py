import pandas as pd

#Removing all empty cells.
df = pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df.to_string())
print()
df.dropna(inplace=True)

#Filling all empty cells with a specific number.
df.fillna(130, inplace=True)
print(df.to_string())

#To fill only one column of data.
df["Maxpulse"].fillna(130, inplace=True)
print(df.to_string())


#Replacing missing values with mean.
x = df["Maxpulse"].mean()
df["Maxpulse"].fillna(x, inplace=True)
print(df.to_string())

#Replacing with median
x = df["Maxpulse"].median()
df["Maxpulse"].fillna(x, inplace=True)
print(df.to_string())

#Replacing missing values with the mode
x = df["Maxpulse"].mode()[0]
df["Maxpulse"].fillna(x, inplace=True)
print(df.to_string())