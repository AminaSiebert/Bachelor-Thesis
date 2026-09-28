# Bachelor-Thesis
Data and scripts for the bachelor thesis "Assessing Contextual Cues that Influence Thermal Perception in Grayscale".

## Data Analysis
The processing steps were:

| Input                     | Script                | Output                                       | Purpose                                                                            |
| ------------------------- | --------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------- |
| Raw files                 | [format.py](Scripts/format.py)             | [data_f.csv](Data/Responses/data_f.csv) and [data_m.csv](Data/Responses/data_m.csv)                   | Converted participants' responses to .csv files.                                   |
| [data_f.csv](Data/Responses/data_f.csv) and [data_m.csv](Data/Responses/data_m.csv) | [combineData_f_and_m.py](Scripts/combineData_f_and_m.py) | [combined.csv](Data/Responses/combined.csv)                                 | Combine both .csv files into one                                                   |
| [combined.csv](Data/Responses/combined.csv)              | [resorting.py](Scripts/resorting.py)          | [Data/Responses/data_realism.csv](data_realism.csv) and [data_thermal_comfort.csv](Data/Responses/data_thermal_comfort.csv) | Remove participants that did not answer all questions and reshape into wide format |
