import pandas as pd

df1 = pd.read_csv("/Users/amina/Downloads/prolific_demographic_export_6a67209937337e137bb8a2a8.csv")
df2 = pd.read_csv("/Users/amina/Downloads/prolific_demographic_export_6a67251f9aadf4996a4329f4.csv")

# Keep only the first 50 entries from each file
df1 = df1.head(50)
df2 = df2.head(50)

combined = pd.concat([df1, df2], ignore_index=True)

combined.to_csv("/Users/amina/Downloads/demographic.csv", index=False)