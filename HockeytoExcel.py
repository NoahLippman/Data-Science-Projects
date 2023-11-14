import pandas as pd 
import csv
import numpy as np

def write_excel_from_csv():
    # Get Data and situation
    d1 = pd.DataFrame(pd.read_csv('/Users/noahlippman/Downloads/skaters.csv'))

    #Get situations
    situations = []
    while True:
        situation = input("In what situation do you want data about (5on5, 4on5, 5on4, all, other) or ALL to get all situations     ")
        if (situation == 'STOP') or (situation== 'ALL'):
            if situation == 'ALLALL':
                situations.append(situation)
            break
        situations.append(situation)


    # Get target players
    target_names = []
    playerName = ''
    while True:
        playerName = input('enter player name or ALL (to use all players), enter STOP to be done    ')
        if (playerName == 'STOP') or (playerName == 'ALL'):
            if playerName == 'ALL':
                target_names.append(playerName)
            break
        target_names.append(playerName)

    # Get stats and print
    coloumnsArray = np.array(d1.columns.values).reshape(2,77)
    print(coloumnsArray)

    # Get users' desired stats
    target_stats = ['playerId',	'season',	'name',	'team',	'position',	'situation',	'games_played',	'icetime']
    while True:
        stat = input('enter stat name or ALL (to use all stats) enter STOP to be done    ')
        if (stat == 'STOP') or (stat == 'ALL'):
            if stat =='ALL':
                target_stats.append(stat)
            break
        target_stats.append(stat)
    print(target_stats)

    # Filter data frame given users' inputs
    filtered_df = d1
    if 'ALL' not in target_names:
        filtered_df = d1[d1['name'].isin(target_names)]
    if 'ALL' not in target_stats:
        filtered_df = filtered_df.drop(columns = [col for col in filtered_df if col not in target_stats])
    if  'ALL' not in situations:
        filtered_df = filtered_df[filtered_df['situation'].isin(situations)]
    print(filtered_df)

    # Save File
    fileSaveName = input('under what name would you like to save your file  ')
    filtered_df.to_excel(f'{fileSaveName}.xlsx')        

if __name__ == "__main__":
    write_excel_from_csv()