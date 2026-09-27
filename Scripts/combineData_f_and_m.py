import pandas as pd

df1 = pd.read_csv("data_f.csv")
df2 = pd.read_csv("data_m.csv")

combined = pd.concat([df1, df2], ignore_index=True)

combined.to_csv("combined.csv", index=False)