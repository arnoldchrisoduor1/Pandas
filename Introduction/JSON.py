import pandas as pd

print()
print("Reading JSON files.")
df = pd.read_json('data.json')
print(df.to_string())
print()