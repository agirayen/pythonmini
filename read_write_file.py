import csv
import pandas as pd

data = { "Name":["John","Luke","Matthew","Mark"],
         "Age":[40,43,45,41] }

data = pd.DataFrame(data)
data.to_csv("Age_data.csv",index=False)
print(data.head())

data = pd.read_csv("Age_data.csv")
print(data.head())
