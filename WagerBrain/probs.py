from fractions import Fraction
from WagerBrain.payouts import decimal_profit, decimal_payout

"""

Calculate Implied Win %'s from American, Decimal, Fractional odds
Calculate Expected Value of a wager

"""


def decimal_implied_win_prob(odds):
    return 1 / odds


def american_implied_win_prob(odds):
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return abs(odds) / (abs(odds) + 100)


def fractional_implied_win_prob(odds):
    odds = Fraction(odds)
    return 1 / ((odds.numerator / odds.denominator) + 1)


def expected_value(stake, profit, win_prob):
    return profit * win_prob - stake * (1 - win_prob)



stake = 100
odds = 1.66
profit = decimal_profit(stake, odds)
payout = decimal_payout(stake, odds)
win = decimal_implied_win_prob(odds)

print("Profit: ", profit)
print("Payout: ", payout)
print("Win Prob: ", win)