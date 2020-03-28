from WagerBrain.odds import decimal_odds


def break_even_pct(stake, payout):
    """
    :param stake: Float. Currency amount wagered.
    :param payout: Float. Currency amount paid out (stake + profit)
    :return: Float. % Amount of time you need to win more than to be profitable. % > 100 because of Vig
    """
    return stake / payout


def vig(f_stake, f_payout, u_stake, u_payout):
    """
    :param f_stake: Float. Amount bet on Favorite.
    :param f_payout: Float. Total payout on Favorite.
    :param u_stake: Float. Amount bet on Underdog.
    :param u_payout: Float. Total payout on Underdog.
    :return: % vig paid to the bookmaker.
    """
    return (break_even_pct(f_stake, f_payout) + break_even_pct(u_stake, u_payout)) - 1


def bookmaker_margin(fav_odds, dog_odds, draw_odds=None):
    """
    :param fav_odds:  Integer. (American), Float(Decimal), String or Fraction Class (Fractional) The odds on offer for the favorite
    :param dog_odds:  Integer. (American), Float(Decimal), String or Fraction Class (Fractional) The odds on offer for the underdog
    :param draw_odds: Integer. (American), Float(Decimal), String or Fraction Class (Fractional) The odds on offer for a tie
    :return: Float. Percentage of wager paying bookmaker margin (bookmaker's edge normalized as % in decimal terms
    """
    if not draw_odds:
        # Formula requires decimal odds
        fav_odds = decimal_odds(fav_odds)
        dog_odds = decimal_odds(dog_odds)

        return ((1 / fav_odds) + (1 / dog_odds)) - 1

    else:
        fav_odds = decimal_odds(fav_odds)
        dog_odds = decimal_odds(dog_odds)
        draw_odds = decimal_odds(draw_odds)

        return ((1 / fav_odds) + (1 / dog_odds) + (1 / draw_odds)) - 1


def bookmaker_commission(fav_odds, dog_odds, commish, draw_odds=None):
    """
    :param fav_odds: Integer (American), Float(Decimal), String or Fraction Class (Fractional). Market odds on favorite
    :param dog_odds: Integer (American), Float(Decimal), String or Fraction Class (Fractional). Market odds on underdog
    :param commish: Float. Betting exchange's commission
    :param draw_odds: Integer (American), Float(Decimal), String or Fraction Class (Fractional). Market odds on a draw outcome if applicable
    :return: Float. % representing true cost / edge to bookmaker, exchange normalized as % in decimal terms
    """
    if not draw_odds:
        fav_odds = decimal_odds(fav_odds)
        dog_odds = decimal_odds(dog_odds)

        fav_odds = 1 + ((1 - (commish / 100)) * (fav_odds - 1))
        dog_odds = 1 + ((1 - (commish / 100)) * (dog_odds - 1))

        return (((1 / fav_odds) * 100 + (1 / dog_odds) * 100) - 100) / 100

    else:
        fav_odds = decimal_odds(fav_odds)
        dog_odds = decimal_odds(dog_odds)
        draw_odds = decimal_odds(draw_odds)

        fav_odds = 1 + ((1 - (commish / 100)) * (fav_odds - 1))
        dog_odds = 1 + ((1 - (commish / 100)) * (dog_odds - 1))
        draw_odds = 1 + ((1 - (commish / 100)) * (draw_odds - 1))

        return (((1 / fav_odds) * 100 + (1 / dog_odds) * 100 + (1 / draw_odds) * 100) - 100) / 100

print(break_even_pct(115,215) + break_even_pct(100,205) - 1)
print(vig(115,215,100,205))