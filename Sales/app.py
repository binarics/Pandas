import pandas as pd

df = pd.read_excel("SampleData.xlsx")
df1 = pd.read_excel("SampleData-TIME.xlsx")

print(df.join(df1))