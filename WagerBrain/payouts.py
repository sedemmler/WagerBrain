from fractions import Fraction


"""

Calculate payouts and profits.
--- Payout = Stake + Profit
--- Profit = Payout - Stake

"""


# Payouts = stake + win (e.g., bet 100 and you win $10 = payout of $110)
def american_payout(odds, stake):
    if odds > 0:
        return (stake * (odds / 100)) + stake
    else:
        return (stake / (odds / 100)) + stake


def decimal_payout(stake, odds):
    return stake * odds


def fractional_payout(stake, odds):
    odds = Fraction(odds)
    return (stake * (odds.numerator / odds.denominator)) + stake


# Profit is whatever incremental gain above your stake that is returned (e.g., $100 pays $110, the profit is $10)
def american_profit(stake, odds):
    if odds > 0:
        return stake * (odds / 100)
    else:
        return stake / (odds / 100)


def decimal_profit(stake, odds):
    return stake * (odds - 1)


def fractional_profit(stake, odds):
    return stake * (odds.numerator / odds.denominator)
