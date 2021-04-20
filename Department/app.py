import pandas as pd

df1 = pd.read_excel("names.xlsx")
df2 = pd.read_excel("department.xlsx")

df2.set_index("ID", inplace=True)

print(df2)

print(df1.join(df2, on="Department_ID", rsuffix="_Department"))

print(df1.merge(df2, how="left", left_on="Department_ID", right_index=True, suffixes="_X"))