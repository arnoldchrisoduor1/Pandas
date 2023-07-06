import pandas as pd

#the duplicate method returns boolean value if data is duplicate or not.
df = pd.read_csv('data.csv')

print(df.duplicated())

#dropping duplicates
df.drop_duplicates(inplace=True)