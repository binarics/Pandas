import pandas as pd

df = pd.read_excel('SampleData.xlsx')

df.set_index("Rep", inplace=True)

print(df.sort_index(axis=1))