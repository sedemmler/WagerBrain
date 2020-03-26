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
    return round((((prob * odds) - 1) / (odds - 1) * kelly_size), 2)
