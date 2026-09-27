# This code resorts the data from a long format to a wide format.

import pandas as pd
from itertools import product

# Read the combined dataset
df = pd.read_csv("Users/amina/Downloads/data/combined.csv")

# remove participants that did not answer all questions
trial_counts = df.groupby("participant_id").size()
missing = trial_counts[trial_counts != 64]

df = df[~df["participant_id"].isin(missing.index)]

# wide format instead of long format
data_wide = (
    df.pivot(
        index="participant_id",
        columns="conditionId",
        values="realism"
    )
    .reset_index()
)

# order conditions and add abbreviations
condition_order = [
    f"{snow}_{clothing}_{animal}_{sun}_{obj}_{fire}"
    for snow, clothing, animal, sun, obj, fire in product(
        ["NS", "S"],
        ["SC", "WC"],
        ["Ca", "Pe"],
        ["SR", "SM"],
        ["Sa", "Sn"],
        ["NF", "WF"],
    )
]

# reorder
data_wide = data_wide[["participant_id"] + condition_order]
# convert to csv
data_wide.to_csv("Users/amina/Downloads/data/data_realism.csv", index=False)