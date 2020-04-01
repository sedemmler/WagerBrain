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
