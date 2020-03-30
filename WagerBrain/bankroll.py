from WagerBrain.odds import decimal_odds
"""

Bankroll management functions

"""


def basic_kelly_criterion(prob, odds, kelly_size=1):
    """
    :param prob: Float. Estimated probability of winning the wager
    :param odds: Integer (American), Float(Decimal), String or Fraction Class (Fractional). Stated odds from bookmaker
    :param kelly_size: Integer. Risk management. (e.g., 1 is Kelly Criterion, .5 is Half Kelly, 2+ is Levered Kelly)
    :return: Float. % of bankroll one should commit to wager
    """
    b = decimal_odds(odds) - 1
    q = 1 - prob
    return ((b * q - prob) / b) * kelly_size


def fibonacci_bankroll(odds, bet_num=1, unit_size=.01):
    """
    :param odds: Integer (American), Float(Decimal), String or Fraction Class (Fractional). Stated odds from bookmaker
    :param bet_num: Integer. How many bets you've made so far
    :param unit_size: Float. % of bankroll wagered per bet
    :return: Float. Fibonacci multiplied bet size
    """
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 100]
    if bet_num > len(fib):
        bet_num = fib[-1]

    if decimal_odds(odds) > 2.618:
        return unit_size * fib[bet_num]
    else:
        return None


def five_bet_labouchere_bankroll(target):
    """
    Pick a target $-amount you want to win. and then make a sequence of bets that follows the ratio output below.

    Each wager must be at odds such that the profit (payout) is the sum of the first and last number in your list.
    If bet 1 wins 20 (.1 + .1) then cross off the first and last numbers.

    If you lose add your stake to the list below.

    :param target: Integer. How much do you want to win?
    :return: List. Sequence of $ amount bets to make.
    """
    labouchere_div = [.1, .2, .4, .2, .1]
    return [target * x for x in labouchere_div]

