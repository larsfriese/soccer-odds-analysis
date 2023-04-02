### Introduction

This is a small project to analyse the odds of the german bundesliga games.
A friend scraped the odds from the german betting site [tipico](https://www.tipico.de/) and recorded their odds hourly.
Now I want to analyse the data and see if there are any interesting insights.

### Preprocessing the data

In the folder ['hourly'](hourly/) we find hourly data of the tipico odds for the next bundesliga games.
These odds were recorded in the period of <b>2022-08-12 to 2022-11-24.</b>
That will include the 2nd up until the 15th matchday of the 2022/23 season. 
The Script ['hourly_to_csv.py'](hourly_to_csv.py) converts the data to a csv file.
After conversion the csv file is approximately <b>25k rows by 20 columns</b> large.

### Analysing the data

What interests me here are the following questions:
- How are the odds generally distributed?
- How much on average do the odds change before a game?
- Is there a correlation between the change of odds and the result of the game?

I answer these questions in the analysis notebook ['analysis.ipynb'](analysis.ipynb).

### Future

I will continue to analyse this data and try to find more interesting insights.
The second part of this project will analyse the odds of german soccer matches <b>during</b> the game.

