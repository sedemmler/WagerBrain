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


def fibonacci_bankroll():
    """
    Only bet on draws when the probability is above 2.618
    Increase your betting stake in a way that follows the Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21 etc.
    """
    pass


def labouchere_bankroll():
    """
    To be profitable in sports betting, staking strategy is as important as finding value odds.
    With many progressive staking systems, such as the Labouchere system, promising almost infinite wealth,
    are they a good idea to follow? Here’s the academic answer to the question.

    The Labouchère staking system is a progressive staking method acording to which a bettor continues to bet until a
    particular winning amount is reached, and is traditionally used for Roulette.

    The Labouchère staking method in sports betting
    Labouchère can be easily extended to sports betting and the steps involved in applying this staking method
    are the following:

    Decide how much money you want to win. Let's aim, for example, to win $100.
    Determine how you will split this money. Say you split it up over five values: $10, $20, $40, $20, $10.
    Place a bet that would win the sum of the first and last numbers. If the European/Decimal odd is
    3 (+200 American/MoneyLine) for example, you would stake $10, so as to win $20 back (the sum of the first and
    last number).
    If you win, you tick off the first and last number. Otherwise, you add the amount of the stake you made, so that you
    need to win this back. In this case, you would have $10, $20, $40, $20, $10 and $10.
    Repeat steps 3 and 4 until you win the amount you are aiming for.
    """
    pass
