from fractions import Fraction
from math import gcd


"""
Convert the style of gambling odds to Function Name (Decimal, American, Fractional).

TO DO: Fix edge case related to Fraction module that causes weird rounding / slightly off output    
"""


def american_odds(odds):
    """
    :param odds: Float (e.g., 2.25) or String (e.g., '3/1' or '5/4').
    :return: Integer. Odds expressed in American terms.
    """
    if isinstance(odds, int):
        return odds

    elif isinstance(odds, float):
        if odds > 2.0:
            return round((odds - 1) * 100, 0)
        else:
            return round(-100 / (odds - 1), 0)

    elif "/" in odds:
        odds = Fraction(odds)

        if odds.numerator > odds.denominator:
            return (odds.numerator / odds.denominator) * 100
        else:
            return -100 / (odds.numerator / odds.denominator)


def decimal_odds(odds):
    """
    :param odds: Integer (e.g., -350) or String (e.g., '3/1' or '5/4').
    :return: Float. Odds expressed in Decimal terms.
    """
    if isinstance(odds, float):
        return odds

    elif isinstance(odds, int):
        if odds >= 100:
            return abs(1 + (odds / 100))
        elif odds <= -101 :
            return 100 / abs(odds) + 1
        else:
            return float(odds)

    elif "/" in odds:
        odds = Fraction(odds)
        return round((odds.numerator / odds.denominator) + 1, 2)


def fractional_odds(odds):
    """
    :param odds: Numeric. (e.g., 2.25 or -350).
    :return: Fraction Class. Odds expressed in Fractional terms.
    """
    if isinstance(odds, str):
        return Fraction(odds)

    elif isinstance(odds, int):
        if odds > 0:
            denom = 100
            g_cd = gcd(odds, denom)
            num = int(odds / g_cd)
            denom = int(denom / g_cd)

            return Fraction(num, denom)

        else:
            num = 100
            g_cd = gcd(num, odds)
            num = int(num / g_cd)
            denom = int(odds / g_cd)

            return -Fraction(num, denom)

    elif isinstance(odds, float):
        new_odds = int((odds - 1) * 100)
        g_cd = gcd(new_odds, 100)
        return Fraction(int(new_odds/g_cd), int(100/g_cd))
