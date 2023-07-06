import pandas as pd

print()
print("Using the header(), attribute to get an overview of the data")
df = pd.read_csv('data.csv')
print(df.head(10))
print()
#If the value for head is not specified, it will return thw first five.
print()
print("Viewing the last 5 rows")
print(df.tail())
print()

print("Getting data information")
print(df.info())
print()