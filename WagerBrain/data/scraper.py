import requests
from bs4 import BeautifulSoup
import pandas as pd


def ken_pom_scrape():
    """
    :return: DataFrame of KenPom's complete College Rankings / Advanced Stats
    """
    url = 'https://kenpom.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    table = soup.table
    table_rows = table.find_all('tr')

    team_rows = list()
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        team_rows.append(row)

    cols = ["Rk", "Team", "Conf", "Record", "AdjEM", "AdjO", "a", "AdjD", "b", "AdjT", "c", "Luck", "d",
            "SoS AdjEM", "e", "OppO", "f", "OppD", "g", "NCOS AdjEM", "h"]

    ken_pom = pd.DataFrame(team_rows[2:], columns=cols)

    ken_pom.drop(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], axis=1, inplace=True)

    ken_pom['Rk'] = ken_pom['Rk'].astype('float')
    ken_pom['AdjEM'] = ken_pom['AdjEM'].astype('float')
    ken_pom['AdjO'] = ken_pom['AdjO'].astype('float')
    ken_pom['AdjD'] = ken_pom['AdjD'].astype('float')
    ken_pom['AdjT'] = ken_pom['AdjT'].astype('float')
    ken_pom['Luck'] = ken_pom['Luck'].astype('float')
    ken_pom['SoS AdjEM'] = ken_pom['SoS AdjEM'].astype('float')
    ken_pom['OppO'] = ken_pom['OppO'].astype('float')
    ken_pom['OppD'] = ken_pom['OppD'].astype('float')
    ken_pom['NCOS AdjEM'] = ken_pom['NCOS AdjEM'].astype('float')

    return ken_pom


def bball_ref_per100():
    url = 'https://www.basketball-reference.com/leagues/NBA_2020_per_poss.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    table = soup.table
    table_rows = table.find_all('tr')

    team_rows = list()
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        team_rows.append(row)

    bball_ref_cols = ['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG_perc', '3P', '3PA',
                      '3_perc', '2P', '2PA', '2_perc', 'FT', 'FTA', 'FT_perc', 'ORB', 'DRB', 'TRB', 'AST',
                      'STL', 'BLK', 'TOV', 'PF', 'PTS', 'None', 'ORtg', 'DRtg']

    per_100_poss = pd.DataFrame(team_rows, columns=bball_ref_cols)

    per_100_poss = per_100_poss.mask(per_100_poss.eq('None')).dropna()

    per_100_poss['Age'] = per_100_poss['Age'].astype('float')
    per_100_poss['G'] = per_100_poss['G'].astype('float')
    per_100_poss['GS'] = per_100_poss['GS'].astype('float')
    per_100_poss['MP'] = per_100_poss['MP'].astype('float')
    per_100_poss['FG'] = per_100_poss['FG'].astype('float')
    per_100_poss['FGA'] = per_100_poss['FGA'].astype('float')
    # per_100_poss['FG_perc'] = per_100_poss['FG_perc'].astype('float')
    per_100_poss['3P'] = per_100_poss['3P'].astype('float')
    per_100_poss['3PA'] = per_100_poss['3PA'].astype('float')
    # per_100_poss['3_perc'] = per_100_poss['3_perc'].astype('float')
    per_100_poss['2P'] = per_100_poss['2P'].astype('float')
    per_100_poss['2PA'] = per_100_poss['2PA'].astype('float')
    # per_100_poss['2_perc'] = per_100_poss['2_perc'].astype('float')
    per_100_poss['FT'] = per_100_poss['FT'].astype('float')
    per_100_poss['FTA'] = per_100_poss['FTA'].astype('float')
    # per_100_poss['FT_perc'] = per_100_poss['FT_perc'].astype('float')
    per_100_poss['ORB'] = per_100_poss['ORB'].astype('float')
    per_100_poss['DRB'] = per_100_poss['DRB'].astype('float')
    per_100_poss['TRB'] = per_100_poss['TRB'].astype('float')
    per_100_poss['AST'] = per_100_poss['AST'].astype('float')
    per_100_poss['STL'] = per_100_poss['STL'].astype('float')
    per_100_poss['BLK'] = per_100_poss['BLK'].astype('float')
    per_100_poss['TOV'] = per_100_poss['TOV'].astype('float')
    per_100_poss['PF'] = per_100_poss['PF'].astype('float')
    per_100_poss['PTS'] = per_100_poss['PTS'].astype('float')
    # per_100_poss['ORtg'] = per_100_poss['ORtg'].astype('float')
    per_100_poss['DRtg'] = per_100_poss['DRtg'].astype('float')

    return per_100_poss


def bball_ref_adv():
    url = 'https://www.basketball-reference.com/leagues/NBA_2020_advanced.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    table = soup.table
    table_rows = table.find_all('tr')

    team_rows = list()
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        team_rows.append(row)

    cols = ['Player', 'Pos', 'Age', 'Tm', 'G', 'MP', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%', 'DRB%', 'TRB%', 'AST%',
            'STL%', 'BLK%', 'TOV%', 'USG%', "NONE", 'OWS', 'DWS', 'WS', 'WS_48', 'NONE', 'OBPM', 'DBPM', 'BPM', 'VORP']

    adv = pd.DataFrame(team_rows, columns=cols)

    adv = adv.mask(adv.eq('NONE')).dropna()

    return adv
