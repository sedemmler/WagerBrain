from WagerBrain.odds import decimal_odds
"""

Bankroll management functions

"""


def basic_kelly_criterion(prob, odds, kelly_size=1):
    """
    :param prob: Estimated probability of winning the wager
    :param odds: Stated odds from bookmaker
    :param kelly_size: Risk management. (e.g., 1 is Kelly Criterion, .5 is Half Kelly, 2+ is Levered Kelly)
    :return: % of bankroll one should commit to wager
    """
    b = odds - 1
    q = 1 - prob
    return ((b * q - prob) / b) * kelly_size
