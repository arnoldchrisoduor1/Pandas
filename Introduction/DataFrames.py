import pandas as pd

print("Creating a data frame")
data = {
    'calories':[450, 700, 964],
    'Duration': [78, 56, 32]
}

print(pd.DataFrame(data))
print()

#Using the loc() attribute to  return 1 or more rows.
import pandas as pd

print("Using the loc attribute")
data = {
    'calories':[450, 700, 964],
    'Duration': [78, 56, 32]
}

myvar = pd.DataFrame(data)
print(myvar.loc[0])
print()

import pandas as pd

print("Naming my own indexes")
data = {
    'calories':[450, 700, 964],
    'Duration': [78, 56, 32]
}

print(pd.DataFrame(data, index = ["day1", "day2", "day3"]))
print()

print("Reading all CSV files")
varr = pd.read_csv('sample.csv')
print(varr)