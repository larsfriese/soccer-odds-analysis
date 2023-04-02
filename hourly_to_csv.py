import pandas as pd
from setuptools import glob
from datetime import datetime

# list with all matches
global_data_list = []

# for each text file in the folder "hourly"
for file in glob.glob("hourly/*.txt"):

    # get the date and time from the filename
    datetime_object = datetime.strptime(file[9:], '%y%m%d%H%M%S.txt')

    # get line 60 until end of file in a list of strings
    lines = open(file).readlines()[59:]

    tage = ["Morgen", "Heute", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    current_day = ""
    data_list = []
    skip_to_next = 0
    current_date = [""]

    # iterate through the lines to get matches
    for c, line in enumerate(lines):

        # if one of the weekdays and/or a date is seen first
        if any(x in line for x in tage):

            # if live game
            if 'LIVE\n' in lines[c:c+20]:
                continue

            # if goal was scored and live is not in string
            # look for the match score
            if len(lines[c+3])==2 and len(lines[c+4])==2:
                continue

            current_day = line
            data_list.append(lines[c:c+20])
            current_date[0] = lines[c]
            continue

        # if number is seen first
        if (':' in line) and (len(line) == 6) and (not any(x in lines[c-1] for x in tage)):
            if current_date[0] == "": current_date[0] = "Heute"
            data_list.append(current_date + lines[c:c+19])


    # remove all \n from the sublist of data_list
    for c, sublist in enumerate(data_list):
        for d, item in enumerate(sublist):
            data_list[c][d] = item.replace("\n", "")

        # add the datetime_object to the beginning of each sublist
        data_list[c] = [datetime_object] + sublist

        # create datetetime object for each match
        if "Heute" in data_list[c][1]:
            data_list[c][1] = datetime.strptime(f'{data_list[c][0].day}.{data_list[c][0].month}.{data_list[c][0].year}'
                                                f' {data_list[c][2]}', '%d.%m.%Y %H:%M')
        else:
            data_list[c][1] = datetime.strptime(f'{data_list[c][1][-5:]}.{data_list[c][0].year} {data_list[c][2]}', '%d.%m.%Y %H:%M')

        # remove 3rd element from sublist
        data_list[c].pop(2)

    # add data_list to global_data_list
    global_data_list.extend(data_list)

# dataframe for all the matches
df = pd.DataFrame(global_data_list, columns=['record_date', 'game_date', 'home_team', 'away_team',
                                             'home_odds', 'draw_odds', 'away_odds', 'over_under', 'over', 'under',
                                             'handicap', 'home', 'draw', 'away', 'both_teams_score_yes',
                                             'both_teams_score_no', 'halftime_over_under', 'over', 'under', 'other_bets'])

# save dataframe to csv
df.to_csv("hourly.csv", index=False)


