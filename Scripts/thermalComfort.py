# This code created Figure 4.2.
# The code was adapted from Christoph Wührl.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/amina/Downloads/data/combined.csv")

# remove participants that did not answer all questions
trial_counts = df.groupby("participant_id").size()
missing = trial_counts[trial_counts != 64]


df_complete = df[~df["participant_id"].isin(missing.index)].copy()


df_complete['thermalComfort'] = df_complete['thermalComfort'].astype(float)

factors = [
    "snow",
    "clothing",
    "animals",
    "sunPosition",
    "sceneObject",
    "fire"
]

# map labels
label_map = {
    "NoSnow": "No Snow",
    "Snow": "Snow",
    "SummerClothing": "Summer",
    "WinterClothing": "Winter",
    "Camels": "Camels",
    "Penguins": "Penguins",
    "SunRising": "Low",
    "SunMid": "High",
    "Sandcastle": "Sandcastle",
    "Snowman": "Snowman",
    "NoFire": "No Fire",
    "Fire": "Fire",
}

df_complete = df_complete.replace(label_map)

label_factors_map = {
    "snow": "Snow",
    "clothing": "Clothing",
    "animals": "Animals",
    "sunPosition": "Sun Position",
    "sceneObject": "Kids' Creation",
    "fire": "Fire",
}

# define order
factor_order = {
    "snow": ["Snow", "No Snow"],
    "clothing": ["Winter", "Summer"],
    "animals": ["Penguins", "Camels"],
    "sunPosition": ["Low", "High"],
    "sceneObject": ["Snowman", "Sandcastle"],
    "fire": ["No Fire", "Fire"],
}

# plotting
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    "font.size": 14.5,
    "axes.titlesize": 20,
    "axes.labelsize": 20,
    "xtick.labelsize": 14.5,
    "ytick.labelsize": 14.5,
})
fig, axes = plt.subplots(1, len(factors), figsize=(16, 5), sharey=True)

for ax, factor in zip(axes, factors):
    sns.pointplot(data=df_complete, x=factor, y='thermalComfort',
                  order = factor_order[factor], ax=ax,
                  linestyle='none', errorbar='se', capsize=0.2,
                  markersize = 4.5, palette = ["#0072B2", "#D55E00"])
    ax.set_title(label_factors_map[factor])
    ax.set_xlabel('')

for ax in axes:
    ax.set_ylim(2.5, 5.5)
    
axes[0].set_ylabel('Thermal Comfort')
plt.tight_layout()
plt.savefig(f"/Users/amina/Downloads/thermalComfort", dpi=300)
plt.show()

