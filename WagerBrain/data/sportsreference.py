from bs4 import BeautifulSoup
import requests
import pandas as pd
"""

Scraping different X-Reference (BasketballReference, FootballReference, etc) sites

"""


def make_soup():
    url = 'https://www.basketball-reference.com/leagues/NBA_2020_per_poss.html'
    response = requests.get(url)
    return BeautifulSoup(response.content, 'lxml')


def nba_reference_df(response):
    # Get DataFrame Column Names
    full_table = response.find_all(class_='thead')
    cols = full_table[0].text.splitlines()[2:]
    cols.remove('3P%')
    cols.remove('Tm')
    cols.remove('Pos')

    # Get and Clean All Column Data
    raw_player = response.find_all(class_='left', attrs={'data-stat': 'player'})
    player = [x.text for x in raw_player]

    raw_age = response.find_all(class_='right', attrs={'data-stat': 'age'})
    age = pd.Series([x.text for x in raw_age]).astype('int')

    raw_g = response.find_all(class_='right', attrs={'data-stat': 'g'})
    g = pd.Series([x.text for x in raw_g]).astype('int')

    raw_gs = response.find_all(class_='right', attrs={'data-stat': 'gs'})
    gs = pd.Series([x.text for x in raw_gs]).astype('int')

    raw_mp = response.find_all(class_='right', attrs={'data-stat': 'mp'})
    mp = pd.Series([x.text for x in raw_mp]).astype('int')

    raw_fg = response.find_all(class_='right', attrs={'data-stat': 'fg_per_poss'})
    fg = pd.Series([x.text for x in raw_fg]).astype('float')

    raw_fga = response.find_all(class_='right', attrs={'data-stat': 'fga_per_poss'})
    fga = pd.Series([x.text for x in raw_fga]).astype('float')

    raw_fg_pct = response.find_all(class_='right', attrs={'data-stat': 'fg_pct'})
    fg_pct = pd.Series([x.text for x in raw_fg_pct])

    raw_fg3 = response.find_all(class_='right', attrs={'data-stat': 'fg3_per_poss'})
    fg3 = pd.Series([x.text for x in raw_fg3]).astype('float')

    raw_fg3a = response.find_all(class_='right', attrs={'data-stat': 'fg3a_per_poss'})
    fg3a = pd.Series([x.text for x in raw_fg3a]).astype('float')

    raw_fg2 = response.find_all(class_='right', attrs={'data-stat': 'fg2_per_poss'})
    fg2 = pd.Series([x.text for x in raw_fg2]).astype('float')

    raw_fg2a = response.find_all(class_='right', attrs={'data-stat': 'fg2a_per_poss'})
    fg2a = pd.Series([x.text for x in raw_fg2a]).astype('float')

    raw_fg2_pct = response.find_all(class_='right', attrs={'data-stat': 'fg2_pct'})
    fg2_pct = pd.Series([x.text for x in raw_fg2_pct])

    raw_ft = response.find_all(class_='right', attrs={'data-stat': 'ft_per_poss'})
    ft = pd.Series([x.text for x in raw_ft]).astype('float')

    raw_fta = response.find_all(class_='right', attrs={'data-stat': 'fta_per_poss'})
    fta = pd.Series([x.text for x in raw_fta]).astype('float')

    raw_ft_pct = response.find_all(class_='right', attrs={'data-stat': 'ft_pct'})
    ft_pct = pd.Series([x.text for x in raw_ft_pct])

    raw_orb = response.find_all(class_='right', attrs={'data-stat': 'orb_per_poss'})
    orb = pd.Series([x.text for x in raw_orb]).astype('float')

    raw_drb = response.find_all(class_='right', attrs={'data-stat': 'drb_per_poss'})
    drb = pd.Series([x.text for x in raw_drb]).astype('float')

    raw_trb = response.find_all(class_='right', attrs={'data-stat': 'trb_per_poss'})
    trb = pd.Series([x.text for x in raw_trb]).astype('float')

    raw_ast = response.find_all(class_='right', attrs={'data-stat': 'ast_per_poss'})
    ast = pd.Series([x.text for x in raw_ast]).astype('float')

    raw_stl = response.find_all(class_='right', attrs={'data-stat': 'stl_per_poss'})
    stl = pd.Series([x.text for x in raw_stl]).astype('float')

    raw_blk = response.find_all(class_='right', attrs={'data-stat': 'blk_per_poss'})
    blk = pd.Series([x.text for x in raw_blk]).astype('float')

    raw_tov = response.find_all(class_='right', attrs={'data-stat': 'tov_per_poss'})
    tov = pd.Series([x.text for x in raw_tov]).astype('float')

    raw_pf_per = response.find_all(class_='right', attrs={'data-stat': 'pf_per_poss'})
    pf_per = pd.Series([x.text for x in raw_pf_per]).astype('float')

    raw_pts_per = response.find_all(class_='right', attrs={'data-stat': 'pts_per_poss'})
    pts_per = pd.Series([x.text for x in raw_pts_per]).astype('float')

    raw_unsure = response.find_all(class_='right iz', attrs={'data-stat': ''})
    unsure = pd.Series([x.text for x in raw_unsure])

    raw_ortg = response.find_all(class_='right', attrs={'data-stat': 'off_rtg'})
    ortg = pd.Series([x.text for x in raw_ortg])

    raw_drtg = response.find_all(class_='right', attrs={'data-stat': 'def_rtg'})
    drtg = pd.Series([x.text for x in raw_drtg])

    nba_df = pd.DataFrame({
        "Player": player,
        "Age": age,
        "G": g,
        "GS": gs,
        "MP": mp,
        "FG": fg,
        "FGA": fga,
        "FG_pct": fg_pct,
        "FG3": fg3,
        "FG3A": fg3a,
        "FG2": fg2,
        "FG2A": fg2a,
        "FG2_pct": fg2_pct,
        "FT": ft,
        "FTA": fta,
        "FT_pct": ft_pct,
        "ORB": orb,
        "DRB": drb,
        "TRB": trb,
        "AST": ast,
        "STL": stl,
        "BLK": blk,
        "TOV": tov,
        "PF_per": pf_per,
        "PTS_per": pts_per,
        "unsure": unsure,
        "ORTG": ortg,
        "DRTG": drtg
    })

    del (nba_df['unsure'])

    return nba_df

response = make_soup()
test = nba_reference_df(make_soup())
print(test)