import pandas as pd

print()
print("Reading a CSV file")
df = pd.read_csv('data.csv')
print(df.to_string())
print()

print("Changing the amoubt of rows that can be returned.")
df = pd.read_csv('sample.csv')
pd.options.display.max_rows = 9999
print(df)
print()