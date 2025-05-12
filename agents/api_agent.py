import yfinance as yf
from fastapi import APIRouter

router = APIRouter()

@router.get("/get_asia_tech_data")
def get_asia_tech_data():
    tickers = ['TSM', 'SSNLF']  # TSMC and Samsung
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d")
        if not hist.empty:
            price_change = (hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2] * 100
            data[ticker] = {
                "close": hist['Close'].iloc[-1],
                "change": round(price_change, 2)
            }
    return data