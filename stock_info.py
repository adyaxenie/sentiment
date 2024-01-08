import yfinance as yf

def stock_info(ticker):
	stock = yf.Ticker(ticker)
	info = stock.fast_info
	keys = ['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage',
	'lastPrice', 'lastVolume', 'marketCap', 'open', 'previousClose',
	'quoteType', 'regularMarketPreviousClose', 'shares',
	'tenDayAverageVolume', 'threeMonthAverageVolume', 'timezone',
	'twoHundredDayAverage', 'yearChange', 'yearHigh', 'yearLow']
	
	rounded_info = {}
	for key in keys:
		value = info.get(key, None)

		if isinstance(value, (int, float)):
			rounded_info[key] = round(value, 2)
		else:
			rounded_info[key] = value
	return rounded_info