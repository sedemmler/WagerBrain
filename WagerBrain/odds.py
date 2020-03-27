from fractions import Fraction
from math import gcd


"""
Convert the style of gambling odds to Function Name (Decimal, American, Fractional).

TO DO: Fix edge case related to Fraction module that causes weird rounding / slightly off output    
"""


def american_odds(odds):
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
    if isinstance(odds, float):
        return odds

    elif isinstance(odds, int):
        if odds > 0:
            return abs(1 + (odds / 100))
        else:
            return (100 / abs(odds) + 1)

    elif "/" in odds:
        odds = Fraction(odds)
        return round((odds.numerator / odds.denominator) + 1, 2)


def fractional_odds(odds):
    if isinstance(odds, str):
        return odds

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
        num = (odds - 1) * 100
        denom = 100
        g_cd = gcd(int(num), denom)
        num = int(num / g_cd)
        denom = int(denom / g_cd)

        return Fraction(num, denom)
