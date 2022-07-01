# SPY-Returns-Comparison
This script outputs a plot of the returns of $SPY since 10-09-2002 both from intraday holding (namely buying at market open and selling at market close, 
ignoring slippage) and buying and holding. We employ the pandas `DataReader(ticker, 'yahoo', start, end)` function to obtain price data for the SPDR S&P 500 ETF Trust, which tracks the S&P 500 
index, by setting `ticker='SPY'`; from `start='10-09-2002'` until `end='30-06-2022'`.
