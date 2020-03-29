from fractions import Fraction
from math import gcd
from WagerBrain.payouts import decimal_profit, decimal_payout
from WagerBrain.odds import fractional_odds, decimal_odds, american_odds
from WagerBrain.utils import break_even_pct

"""

Calculate Implied Win %'s from American, Decimal, Fractional odds
Calculate Expected Value of a wager
Calculate Odds (Amer, Dec, Frac) from Implied Win %'s

"""


def decimal_implied_win_prob(odds):
    """
    :param odds: Float. Odds expressed in Decimal terms.
    :return: Float. The implied win % of stated odds.
    """
    return round(1 / decimal_odds(odds), 3)


def american_implied_win_prob(odds):
    """
    :param odds: Integer. Odds expressed in American terms.
    :return: Float. The implied win % of stated odds.
    """
    if odds > 0:
        return round(100 / (american_odds(odds) + 100), 3)
    else:
        return round(abs(american_odds(odds)) / (abs(american_odds(odds)) + 100), 3)


def fractional_implied_win_prob(odds):
    """
    :param odds: String (e.g., '3/1') or Python Fraction Class.
    :return: Float. The implied win % of stated odds.
    """
    odds = fractional_odds(odds)
    return round(1 / ((odds.numerator / odds.denominator) + 1), 3)


def stated_odds_ev(stake_win,  profit_win, stake_lose, profit_lose):
    """
    This is the Expected Value (ev) derived from stated odds at a bookmaker. It uses implied win % break-evens. This adds to more than
    100% because it incorporates the Vig. Use "true_odds_ev" to plug in user-calculated odds.
    Most stated odds will produce negative EV. The edge is in your own work and could be seen in true_odds_ev.
    :param stake_win: Float. Amount wagered on FAVORITE.
    :param profit_win: Float. Net amount won on FAVORITE.
    :param stake_lose: Float. Float. Amount wagered on UNDERDOG.
    :param profit_lose: Float. Net amount won on UNDERDOG.
    :return: Float. The expected value of wagering on winner.
    """
    payout_win = stake_win + profit_win
    payout_lose = stake_lose + profit_lose

    win_prob = break_even_pct(stake_win, payout_win)
    lose_prob = break_even_pct(stake_lose, payout_lose)

    return (win_prob * profit_win) - (lose_prob * stake_win)


def true_odds_ev(stake, profit, prob):
    """
    This is the Expected Value (ev) derived from user-calculated odds. For EV on stated odds and implied win % from a
    bookmaker, use 'stated_odds_ev.
    :param stake: Float. Amount wagered.
    :param profit: Float. Net amount returned by wager.
    :param prob: Float. % chance of winning outcome.
    :return: Float. The expected value of wagering on winner.
    """
    return (profit * prob) - (stake * (1 - prob))


def win_prob_to_odds(prob, odds_style="a"):
    """
    :param prob: Float. Implied winning % of a given wager
    :param odds_style: Integer (American), Float(Decimal), String or Fraction Class (Fractional)
    :return: The stated odds of a bet in a given style
    """
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


def elo_prob(elo_diff):
    """
    :param elo_diff: Team A’s ELO rating minus Team B’s ELO rating, plus or minus the difference in several adjustments
    :return: % win probability for Team A
    """
    return 1 / (10**(-elo_diff/400) + 1)
