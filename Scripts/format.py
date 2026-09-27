# This code is used to create a .csv file out of the different folders.

import os
import json
import pandas as pd


DATA_FOLDER = "female"

rows = []
# iterate over participant folders
for participant_folder in os.listdir(DATA_FOLDER):
    folder_path = os.path.join(DATA_FOLDER, participant_folder)
    if not os.path.isdir(folder_path):
        continue
    json_path = None
    for file in os.listdir(folder_path): # search for json file
        if file.endswith(".json"):
            json_path = os.path.join(folder_path, file)
            break
    if json_path is None:
        continue


    # load json
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # extract id
    participant_id = data["prolificPid"]

    # extract submissions
    for i, submission in enumerate(data["submissions"]):

        # get factors
        factors = submission["factors"]

        row = {
            "participant_id": participant_id,
            "submission_index": i,

            "conditionId": submission["conditionId"],
            "fileName": submission["fileName"],

            "thermalComfort": submission.get("thermalComfort"),
            "realism": submission.get("realism"),

            "snow": factors["snow"],
            "clothing": factors["clothing"],
            "animals": factors["animals"],
            "sunPosition": factors["sunPosition"],
            "sceneObject": factors["sceneObject"],
            "fire": factors["fire"],

            "submittedAt": submission["submittedAt"]
        }

        rows.append(row)

# convert to csv
df = pd.DataFrame(rows)
df.to_csv("data_f.csv", index=False)

print(df.head())
print(f"Saved {len(df)} rows")