# yfinance code goes here

### Basic yfinance example first
import yfinance as yf
import pandas as pd

def get_stock_info(ticker_symbol):
    # Fetch stock data
    stock = yf.Ticker(ticker_symbol)

    # Get current stock price
    current_price = stock.history(period="1d")['Close'][0]

    # Get past 30 days of stock prices
    past_30_days = stock.history(period="1mo")['Close'].reset_index()
    past_30_days['Date'] = pd.to_datetime(past_30_days['Date']).dt.strftime('%Y-%m-%d').tolist()
    past_30_days = past_30_days.to_dict(orient='records')
    
    return current_price, past_30_days