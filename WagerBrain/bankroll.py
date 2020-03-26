"""

Bankroll management functions

"""


def basic_kelly_criterion(prob, odds):
    return round(((prob * odds) - 1) / (odds - 1), 2)

