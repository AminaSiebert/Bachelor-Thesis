# This code first calculates the differences between to ratings of snow and no snow for each participant and then calculates the mean and standard deviations.
# Afterwards the same is done for kids' creations.
import pandas as pd

df = pd.read_csv("/Users/amina/Downloads/data/combined.csv")

# 1. Snow
# mean snow and no snow rating for each participant
participant_snow = (
    df.groupby(["participant_id", "snow"])["thermalComfort"]
    .mean()
    .unstack()
)

# calculate difference for each participant
participant_snow["difference"] = (
    participant_snow["Snow"] - participant_snow["NoSnow"]
)

# mean and standard deviation
snow_mean_difference = participant_snow["difference"].mean()
snow_sd_difference = participant_snow["difference"].std()

print("Snow:")
print(f"Mean difference = {snow_mean_difference}")
print(f"SD = {snow_sd_difference}")


# 2. Kids' Creations
# mean snowman and sandcastle rating for each participant
participant_creation = (
    df.groupby(["participant_id", "sceneObject"])["thermalComfort"]
    .mean()
    .unstack()
)

# calculate difference for each participant
participant_creation["difference"] = (
    participant_creation["Snowman"]
    - participant_creation["Sandcastle"]
)

# mean and standard deviation
creation_mean_difference = participant_creation["difference"].mean()
creation_sd_difference = participant_creation["difference"].std()

print("Kids' Creations:")
print(f"mean = {creation_mean_difference}")
print(f"SD = {creation_sd_difference}")