import pandas as pd

df = pd.read_excel("./pokemon_data.xlsx")

print(df.iloc[:,0:5].sort_values(["Name", "Type 2"]))