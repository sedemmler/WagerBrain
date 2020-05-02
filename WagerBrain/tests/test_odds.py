from WagerBrain.odds import *


def test_american_odds():
    decimal = american_odds(1.91)
    frac = american_odds("5/1")
    assert decimal == -110.0
    assert frac == 500.0


def test_decimal_odds():
    amer = round(decimal_odds(-110),2)
    frac = decimal_odds("5/1")
    assert amer == 1.91
    assert frac == 6

def test_fractional_odds():
    amer = fractional_odds(500)
    decimal = fractional_odds(6.0)
    assert amer == 5
    assert decimal == 5


def test_parlary_odds():
    par = parlay_odds([500, -110, 250])
    assert round(par, 2) == 40.09