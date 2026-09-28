# Bachelor-Thesis
Data and scripts for the bachelor thesis "Assessing Contextual Cues that Influence Thermal Perception in Grayscale".

## Data Analysis
The processing steps were:

| Input                     | Script                | Output                                       | Purpose                                                                            |
| ------------------------- | --------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------- |
| [raw_data](Data/Responses/raw_data.zip)                 | [format.py](Scripts/format.py)             | [data_f.csv](Data/Responses/data_f.csv) and [data_m.csv](Data/Responses/data_m.csv)                   | Converted participants' responses to .csv files.                                   |
| [data_f.csv](Data/Responses/data_f.csv) and [data_m.csv](Data/Responses/data_m.csv) | [combineData_f_and_m.py](Scripts/combineData_f_and_m.py) | [combined.csv](Data/Responses/combined.csv)                                 | Combine both .csv files into one                                                   |
| [combined.csv](Data/Responses/combined.csv)              | [resorting.py](Scripts/resorting.py)          | [Data/Responses/data_realism.csv](data_realism.csv) and [data_thermal_comfort.csv](Data/Responses/data_thermal_comfort.csv) | Remove participants that did not answer all questions and reshape into wide format |

## Calculating Mean and Standard Deviation of Participants' Ages
The processing steps were:
| Input           | Script              | Output                          | Purpose                                   |
| --------------- | ------------------- | ------------------------------- | ----------------------------------------- |
| [raw_data](Data/Demographic/rawdata)       | [join_demographic.py](Scripts/join_demographic.py) | [demographic.csv](Data/Demographic/demographic.csv)                 | combine both .csv files into one          |
| [demographic.csv](Data/Demographic/demographic.csv) | [getAges.py](Scripts/getAges.py)          | mean age and standard deviation | calculate mean age and standard deviation |

## Creating The Diagrams
- [combinationsDiagram.py](Scripts/combinationsDiagram.py) generated Figure 4.1, which shows the mean thermal comfort and perceived realism ratings for each cue combination.
- [thermalComfort.py](thermalComfort.py) generated Figure 4.2., which shows the mean imagined thermal comfort rating and standard error for each contextual cue.
- [realism.py](realism.py) generated Figure 4.3., which shows the mean realism rating and standard error for each contextual cue.

## Calculating Mean Difference and Standard Deviation for Snow and Kids' Creations
- [meanDifference.py](Scripts/meanDifference.py) calculated the mean and standard deviation of the rating differences of thermal comfort for snow and kids' creations.
