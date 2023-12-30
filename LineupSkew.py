import pandas as pd
import numpy as np
import matplotlib.pyplot as py
import math
import robustats as rob
from statsmodels.stats.weightstats import DescrStatsW

mlb_teams = {'angels':'LAA', 'astros':'HOU', 
'athletics':'OAK', 'blue-jays':'TOR',
 'brewers':'MIL', 'braves':"ATL",
  'cardinals':"STL", 'cubs':"CHC",
   'diamondbacks':"ARI", 'dodgers':"LAD",
    'giants':"SFG", 'guardians':"CLE",
     'mariners':'SEA', 'marlins':"MIA",
      'mets':"NYM", 'nationals':"WSN",
       'orioles':"BAL", 'padres':"SDP",
        'phillies':"PHI", 'pirates':"PIT",
         'rangers':"TEX", 'rays':"TBR",
          'reds':"CIN", 'red-sox':"BOS",
           'rockies':"COL", 'royals':"KCR",
            'tigers':"DET", 'twins':"MIN",
             'white-sox':"CHW", 'yankees':"NYY"}


# Function to collect Hitting data for each MLB team
def collect_team_data(team):
    data = pd.read_html('https://www.fangraphs.com/teams/' + team)
    dF = pd.DataFrame(data[10])
    dataFrame = dF.drop(dF.index[len(dF) - 1]) 
    return dataFrame

def compute_skew(data):
    values = [value for value in (data['wRC+'].tolist()) if not math.isnan(value)]
    weights = [weight for weight in (data['PA'].tolist()) if weight > 0]
    weightedMean = np.average(values, weights = weights)
    weightedMedian = rob.weighted_median(values,weights)
    standardDeviation = DescrStatsW(values,weights = weights).std
    skew = (3 * (weightedMean - weightedMedian))/standardDeviation
    return (skew,values)

def scrape_runs():
    data = pd.read_html('https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&lg=all&qual=0&type=8&season=2023&month=0&season1=2023&ind=0&team=0,ts&rost=&age=&filter=&players=0')
    return data
# Plot relationship of wrc+ and runs
def wrcVsruns():
    data = pd.read_html('https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&lg=all&qual=0&type=8&season=2023&month=0&season1=2023&ind=0&team=0,ts&rost=&age=&filter=&players=0')
    return data

if __name__ == "__main__":
    skewData = []
    valuesData = []
    # Loop to collect all Hitting data for each MLB team
    for team in mlb_teams:
        skew,values = (compute_skew(collect_team_data(team)))
        skewData.append(skew)
        valuesData.append(values)
    df = pd.DataFrame(skewData, index = mlb_teams)
    print(df)
    # df.to_excel('balanceDataFromPython.xlsx')
