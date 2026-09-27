# This code was adapted from Christoph Wührl.
# It generates the diagram showing the thermal comfort and realism ratings of all contextual cue combinations.
from itertools import product
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/amina/Downloads/data/combined.csv")

# remove participants that did not answer all questions
trial_counts = df.groupby("participant_id").size()
missing = trial_counts[trial_counts != 64]

df_complete = df[~df["participant_id"].isin(missing.index)].copy()

df_complete['thermalComfort'] = df_complete['thermalComfort'].astype(float)
df_complete['realism'] = df_complete['realism'].astype(float) - 4

label_map = {
    "NoSnow": "NS",
    "Snow": "WS",
    "SummerClothing": "SC",
    "WinterClothing": "WC",
    "Camels": "CA",
    "Penguins": "PE",
    "SunRising": "SL",
    "SunMid": "SH",
    "Sandcastle": "SC",
    "Snowman": "SM",
    "NoFire": "NF",
    "Fire": "WF",
}

df_complete = df_complete.replace(label_map)


# Build all combinations
levels = {
    "snow": ["NS", "WS"],
    "clothing": ["SC", "WC"],
    "animals": ["CA", "PE"],
    "sunPosition": ["SL", "SH"],
    "sceneObject": ["SM", "SC"],
    "fire": ["NF", "WF"]
}
# create every possible combination from levels
combos = list(product(*levels.values()))
combo_labels = ['/'.join(c) for c in combos]

dfs = []
for combo in combos:
    mask = pd.Series(True, index=df_complete.index)

    for col, val in zip(levels.keys(), combo):
        mask &= df_complete[col] == val

    subset = df_complete[mask].copy()

    if len(subset) == 0:
        continue

    subset['combo'] = '/'.join(combo)
    dfs.append(subset)

df_plot = pd.concat(dfs)

n_combos = df_plot['combo'].nunique()

# sort by mean thermal comfort
combo_order = (
    df_plot.groupby('combo')['thermalComfort']
    .mean()
    .sort_values(ascending=True)
    .index.tolist()
)

# split
half = (len(combo_order) + 1) // 2
left_order = combo_order[:half]
right_order = combo_order[half:]

fig = plt.figure(
    figsize=(13, half * 0.45)
)
# defide into two big section
outer = fig.add_gridspec(
    1,
    2,
    wspace= -0.12
)

# three sections within each big section
left = outer[0].subgridspec(
    1,
    3,
    width_ratios=[2.3, 2, 2],
    wspace=0.12
)

right = outer[1].subgridspec(
    1,
    3,
    width_ratios=[2.3, 2, 2],
    wspace=0.12
)


ax_label_left = fig.add_subplot(left[0])
ax_tc_left = fig.add_subplot(left[1])
ax_real_left = fig.add_subplot(left[2])

ax_label_right = fig.add_subplot(right[0])
ax_tc_right = fig.add_subplot(right[1])
ax_real_right = fig.add_subplot(right[2])


def plot_half(order, ax_labels, ax_tc, ax_real):

    ax_labels.set_xlim(0, 1)
    ax_labels.set_ylim(len(order) - 0.5, -0.5)
    ax_labels.set_facecolor("none")
    ax_labels.patch.set_alpha(0)

    ax_labels.set_xticks([])
    ax_labels.set_yticks(range(len(order)))

    ax_labels.set_yticklabels(
        order,
        fontsize=8,
        ha="right"
    )
    ax_labels.tick_params(
        axis="y",
        length=0,
        pad=4
    )
    ax_labels.yaxis.tick_right()

    for spine in ax_labels.spines.values():
        spine.set_visible(False)


    # thermal comfort
    sns.pointplot(
        data=df_plot,
        y='combo',
        x='thermalComfort',
        order=order,
        ax=ax_tc,
        linestyle='none',
        errorbar='ci',
        capsize=0.1,
        err_kws={"linewidth": 1.5},
        color="#0072B2",
        markersize=3.5
    )

    ax_tc.set_xlim(1, 7)
    ax_tc.set_xticks(range(1, 8))

    ax_tc.grid(
        axis='x',
        alpha=0.3
    )

    ax_tc.set_xlabel(
        ""
    )

    ax_tc.set_ylabel("")
    ax_tc.set_yticklabels([])

    ax_tc.set_title(
        "Thermal Comfort"
    )

    # realism
    sns.pointplot(
        data=df_plot,
        y='combo',
        x='realism',
        order=order,
        ax=ax_real,
        linestyle='none',
        errorbar='ci',
        capsize=0.1,
        err_kws={"linewidth": 1.5},
        color="#0072B2",
        markersize=3.5
    )

    ax_real.set_xlim(-3, 3)
    ax_real.set_xticks(range(-3, 4))

    ax_real.grid(
        axis='x',
        alpha=0.3
    )

    ax_real.set_xlabel(
        ""
    )

    ax_real.set_ylabel("")
    ax_real.set_yticklabels([])

    ax_real.set_title(
        "Realism"
    )


# plotting
plot_half(
    left_order,
    ax_label_left,
    ax_tc_left,
    ax_real_left
)
plot_half(
    right_order,
    ax_label_right,
    ax_tc_right,
    ax_real_right
)
plt.subplots_adjust(
    left=0.03,
    right=0.99,
    top=0.97,
    bottom=0.06
)
plt.savefig(
    "/Users/amina/Downloads/bigDiagram.png",
    dpi=300,
    bbox_inches="tight",
    pad_inches=0.02
)
plt.show()