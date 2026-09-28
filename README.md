# Bachelor-Thesis
Data and scripts for the bachelor thesis "Assessing Contextual Cues that Influence Thermal Perception in Grayscale".

## Data Analysis
The processing steps were:

| Input                     | Script                | Output                                       | Purpose                                                                            |
| ------------------------- | --------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------- |
| Raw files                 | [format.py](scripts/format.py)             | [data_f.csv](scripts/data_f.csv) and [data_m.csv](scripts/data_m.csv)                   | Converted participants' responses to .csv files.                                   |
| [data_f.csv](scripts/data_f.csv) and [data_m.csv](scripts/data_m.csv) | [combineData_f_and_m.py](scripts/combineData_f_and_m.py) | [combined.csv](combined.csv)                                 | Combine both .csv files into one                                                   |
| [combined.csv](combined.csv)              | [resorting.py](scripts/resorting.py)          | [data_realism.csv](data_realism.csv) and [data_thermalComfort.csv](data_thermalComfort.csv) | Remove participants that did not answer all questions and reshape into wide format |
