from WagerBrain.payouts import *


def test_american_payout():
    neg = american_payout(100, -110)
    pos = american_payout(100, 200)
    assert pos == 300
    assert round(neg, 2) == 190.91


def test_american_profit():
    neg = american_profit(100, -110)
    pos = american_profit(100, 200)
    assert pos == 200
    assert round(neg, 2) == 90.91


def test_decimal_payout():
    assert decimal_payout(100, 2) == 200


def test_decimal_profit():
    assert decimal_profit(100, 2) == 100


def test_fractional_payout():
    assert fractional_payout(100, "5/1") == 600.0
    assert fractional_profit(100, "1/4") == 25.0


def test_parlay_profits():
    pass


def test_parlay_payouts():
    pass
