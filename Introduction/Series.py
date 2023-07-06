import pandas as pd

#Pandas series is a 1-D array holding data of any type.
print()
a = [4, 5, 67, 81]

myvar = pd.Series(a)
print(myvar)
print()

print("Creating my own indices for the data")
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print()

print("Pandas series from a dictionary")
calories = {"day1": 420, "day2": 380, "day3": 390}
print(pd.Series(calories))
print()

print("Creating series from a portion of dictionary")
calories = {"day1": 420, "day2": 380, "day3": 390}
print(pd.Series(calories, index=["day1", "day2"]))
print()