from fractions import Fraction
from WagerBrain.odds import parlay_odds
"""

Calculate payouts and profits.
--- Payout = Stake + Profit
--- Profit = Payout - Stake

"""


def american_payout(stake, odds):
    if odds > 0:
        return (stake * (odds / 100)) + stake
    else:
        return abs((stake / (odds / 100))) + stake


def decimal_payout(stake, odds):
    return stake * odds


def fractional_payout(stake, odds):
    odds = Fraction(odds)
    return (stake * (odds.numerator / odds.denominator)) + stake


def american_profit(stake, odds):
    if odds > 0:
        return stake * (odds / 100)
    else:
        return abs(stake / (odds / 100))


def decimal_profit(stake, odds):
    return stake * (odds - 1)


def fractional_profit(stake, odds):
    odds = Fraction(odds)
    return stake * (odds.numerator / odds.denominator)


def get_payout(odds, stake, odds_style='a'):
    try:
        if odds_style.lower() == "american" or odds_style.lower() == 'amer' or odds_style.lower() == 'a':
            return american_payout(stake, odds)

        elif odds_style.lower() == "decimal" or odds_style.lower() == 'dec' or odds_style.lower() == 'd':
            return decimal_payout(stake, odds)

        elif odds_style.lower() == "fractional" or odds_style.lower() == 'frac' or odds_style.lower() == 'f':
            return fractional_payout(stake, odds)

    except (ValueError, KeyError, NameError):
        return None


def get_profit(odds, stake, odds_style='a'):
    try:
        if odds_style.lower() == "american" or odds_style.lower() == 'amer' or odds_style.lower() == 'a':
            return american_profit(stake, odds)

        elif odds_style.lower() == "decimal" or odds_style.lower() == 'dec' or odds_style.lower() == 'd':
            return decimal_profit(stake, odds)

        elif odds_style.lower() == "fractional" or odds_style.lower() == 'frac' or odds_style.lower() == 'f':
            return fractional_profit(stake, odds)

    except (ValueError, KeyError, NameError):
        return None


def parlay_profit(odds, stake):
    """
    :param odds: List. A list of odds for wagers to be included in parlay
    :param stake: Float. How much cash you're throwing down on this ill-advised parlay
    :return: Float. Net profit = profit - stake
    """
    odds = parlay_odds(odds)
    return (odds * stake) - stake


def parlay_payout(odds, stake):
    """
    :param odds: List. A list of odds for wagers to be included in parlay
    :param stake: Float. How much cash you're throwing down on this ill-advised parlay
    :return: Float. Your total payout (stake + profit)
    """
    odds = parlay_odds(odds)
    return odds * stake
