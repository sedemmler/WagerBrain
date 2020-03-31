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
 - Scrapers to gather data (Basketball Reference, etc.)
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
Scraper Example
```
nba_reference_df(make_soup())
>>>>
                       Player  Age   G  GS  ...  PF_per  PTS_per  ORTG DRTG
0                Steven Adams   26  58  58  ...     3.5     19.7   123  106
1                 Bam Adebayo   22  65  65  ...     3.6     23.1   117  106
2           LaMarcus Aldridge   34  53  53  ...     3.5     27.4   115  113
3    Nickeil Alexander-Walker   21  41   0  ...     4.2     19.5    91  113
4               Grayson Allen   24  30   0  ...     3.4     20.7   111  115
..                        ...  ...  ..  ..  ...     ...      ...   ...  ...
619            Thaddeus Young   31  64  16  ...     4.1     20.0   101  108
620                Trae Young   21  60  60  ...     2.3     39.1   114  117
621               Cody Zeller   27  58  39  ...     5.2     24.0   116  111
622                Ante Žižić   23  22   0  ...     5.9     21.1   116  113
623               Ivica Zubac   22  64  62  ...     6.0     20.8   132  104
```