# This code was used to calculated mean and standard deviation of participants' ages.
import pandas as pd

df = pd.read_csv("/Users/amina/Downloads/demographic.csv")

df["Age"] = pd.to_numeric(df["Age"])

# remove missing age values
ages = df["Age"]

std_age = ages.std()
mean_age = ages.mean()

print(f"Mean age: {mean_age}")
print(f"Standard deviation: {std_age}")