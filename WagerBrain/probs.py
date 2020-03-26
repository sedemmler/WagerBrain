from fractions import Fraction
from math import gcd
from WagerBrain.payouts import decimal_profit, decimal_payout

"""

Calculate Implied Win %'s from American, Decimal, Fractional odds
Calculate Expected Value of a wager
Calculate Odds (Amer, Dec, Frac) from Implied Win %'s

"""
# TODO: Fix issue properly representing fractions across all modules in package.
# TODO: (part 1) EV acts perfect with harcoded values but returns strange results when passing the result of other
# TODO: (part 2) module, even though the other modules return proper results.


def decimal_implied_win_prob(odds):
    return round(1 / odds, 3)


def american_implied_win_prob(odds):
    if odds > 0:
        return round(100 / (odds + 100), 3)
    else:
        return round(abs(odds) / (abs(odds) + 100), 3)


def fractional_implied_win_prob(odds):
    odds = Fraction(odds)
    return round(1 / ((odds.numerator / odds.denominator) + 1), 3)


def expected_value(stake, profit, win_prob):
    return profit * win_prob - stake * (1 - win_prob)


def win_prob_to_odds(prob, odds_style="a"):
    try:
        if odds_style.lower() == "american" or odds_style.lower() == 'amer' or odds_style.lower() == 'a':
            if prob >= .50:
                return int(prob / (1 - prob) * -100)
            else:
                return int((1 - prob) / prob * 100)

        elif odds_style.lower() == "decimal" or odds_style.lower() == 'dec' or odds_style.lower() == 'd':
            return round((100 / prob) / 100, 2)

        elif odds_style.lower() == "fractional" or odds_style.lower() == 'frac' or odds_style.lower() == 'f':
            return Fraction((1 / prob) - 1).limit_denominator()


    except (ValueError, KeyError, NameError):
        return None
