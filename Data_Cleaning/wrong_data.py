import pandas as pd

#Replacing a value in row seven:
df = pd.read_csv('data.csv')
df.loc[7, 'Duration'] = 45

#Replacing multiple values using certain restrains or conditions.
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, 'Duration'] = 60

#Dropping rows less than 120 value in a certain column
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.drop(x, inplace = True)