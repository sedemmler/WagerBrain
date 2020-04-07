# WagerBrain
A package containing the essential math and tools required for sports betting and gambling. Once you've scraped odds from Covers.com, Pinnacle, Betfair, or wherever, import WagerBrain and start hunting for value bets.

![Image of The Big Board](https://miro.medium.com/max/1312/1*bGOGcEPpsa0tetM5u-J9NA.jpeg)

**Phase 1 (_complete_):** 
 - Convert Odds between American, Decimal, Fractional
 - Convert Odds to Implied Win Probabilities and back to Odds
 - Calculate Profit and Total Payouts
 - Calculate Expected Value
 - Calculate Kelly Criterion
 - Calculate Parlay Odds, Total Payout, Profit

 
 **Phase 2 (_complete_):**
 - Evaluate Wager-Arbitrage Opportunities
 - Calculate bookmaker spread/cost
 - Calculate the Bookmaker's Vig
 - Calculate Win Probability from a team's ELO (538-style)

 
 **Phase 3 (_in progress_):**
 - Scrapers to gather data (Basketball Reference, KenPom etc.)  [_Partially implemented_]
 - Clean up functions into logical classes
 - Value Bets (take in sets of odds, probabilities and output the most effective betting implementation)
 - Scan for Arbitrage (search scrape bookmakers to feed into Phase 2's Arbitrage evaluator)
 - Visualization (compare all wager opportunities, et al)
 
  **Phase 4 (_not started_):**
  - Automation and Intelligence (e.g., Using phases 1-3 as tools, develop ML and AI models to make predictions, manage bankroll, execute bets)

# Examples

Parlay 3 wagers from different sites offering different odds-styles:
```
odds = [1.91, -110, '9/10']
parlay_odds(odds)
>>>> 6.92
```
No clue how to read decimal odds because you're American? (wager * decimals odds, though...super simple), then convert them back to American-style odds:
```
american_odds(6.92)
>>>> +592
``` 
What's the Vig on the Yankees vs Dodgers?
```
Yankees -115
Dodgers +105
Betting 115 to win 100 on Yankees
Betting 100 to win 205 on Dodgers

vig(115,215,100,205)
>>>> 2.26%
```
Arbitrage Example
```
            5Dimes	Pinnacle
Djokovic    *1.360*	1.189
Nadal	    3.170	*5.500*

odds = [1.36, 5.5]
stake = 1000
basic_arbitrage(odds, stake)

>>>> Bet $801.53 on Djokovic
>>>> Bet $198.47 on Nadal
>>>> Win $90.51 regardless of the outcome
```
KenPom NCAAB Scraper
```
ken_pom_scrape()
>>>>
        Rk                    Team  Conf  ...   OppO   OppD  NCOS AdjEM
0      1.0                  Kansas   B12  ...  107.4   94.7        9.58
1      2.0                 Gonzaga   WCC  ...  103.5  101.0       -2.09
2      3.0                  Baylor   B12  ...  106.4   96.2        1.38
3      4.0                  Dayton   A10  ...  104.1  101.3       -0.74
4      5.0                    Duke   ACC  ...  106.0   98.7        2.60
..     ...                     ...   ...  ...    ...    ...         ...
364  349.0  Maryland Eastern Shore  MEAC  ...   97.6  104.1        7.78
365  350.0                  Howard  MEAC  ...   96.7  105.0        0.96
366  351.0  Mississippi Valley St.  SWAC  ...   97.8  103.9        5.14
367  352.0            Kennesaw St.  ASun  ...  102.0  103.7        4.10
368  353.0             Chicago St.   WAC  ...  100.6  104.3       -0.75
```
