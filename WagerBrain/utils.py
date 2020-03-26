from WagerBrain.odds import decimal_odds


def bookmaker_margin(fav_odds, dog_odds):
    """
    :param fav_odds:  The odds on offer for the favorite
    :param dog_odds:  The odds on offer for the underdog
    :return: Percentage of wager paying bookmaker margin (commission)
    """

    # Formula requires decimal odds
    fav_odds = decimal_odds(fav_odds)
    dog_odds = decimal_odds(dog_odds)

    return round(((1 / fav_odds) + (1 / dog_odds)) / 100, 2)
