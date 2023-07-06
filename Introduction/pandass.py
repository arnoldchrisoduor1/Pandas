import pandas as pd

mydata = {
    'cars':["Volvo", "BMW", "Audi"],
    'passing': [3, 7, 6]
}

myvar = pd.DataFrame(mydata)
print(myvar)
print()
