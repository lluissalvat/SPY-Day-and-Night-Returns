# SPY-Returns-Comparison
This script outputs a plot of the returns of $SPY since 10-09-2002 both from intraday holding (namely buying at market open and selling at market close, 
ignoring slippage and taxes) and buying and holding (namely buying at the adjusted market close price and buying at the adjusted market close price of the next day, which is equivalent to buying at the adjusted close price of the first day and computing the holding return of each day; denoted in the script as `data['Day and Night Returns']`). 

We employ the pandas `DataReader(ticker, 'yahoo', start, end)` function to obtain price data for the SPDR S&P 500 ETF Trust, which tracks the S&P 500 
index, by setting `ticker='SPY'`; from `start='10-09-2002'` until `end='30-06-2022'`. We first calculate the returns by multiples of the initial price and then transform it to percentage returns. Feel free to run the script and modify the ticker and the start and end date.

From the plot obtained by running the script, we see that the intraday holding strategy has returned around 65.65% (CAGR of 2.58%), whereas the buy and hold strategy has returned around 606.30% (CAGR of 10.38%). We can thus conclude that the vast majority of the returns of $SPY during the aforementioned dates happened not during the trading day, but during after-hours trading and the pre-market.
