import yfinance as yf

def fetch_data(tickers):
    return {ticker: yf.Ticker(ticker).info for ticker in tickers}